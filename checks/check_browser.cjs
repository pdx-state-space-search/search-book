#!/usr/bin/env node
/* Render/layout smoke check for the generated mdBook.
 * Requires Chromium and the Debian node-ws package, or equivalent.
 * Screenshots go to a temporary directory, not the book source.
 */
const fs = require('node:fs/promises');
const path = require('node:path');
const os = require('node:os');
const {spawn} = require('node:child_process');
const WebSocket = require('ws');
const {pathToFileURL} = require('node:url');
const root = path.resolve(__dirname, '..');
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));

(async () => {
  const tmp = await fs.mkdtemp(path.join(os.tmpdir(), 'search-book-browser-'));
  const profile = path.join(tmp, 'profile');
  const child = spawn(process.env.CHROMIUM || 'chromium', [
    '--headless', '--no-sandbox', '--disable-gpu', '--no-first-run',
    '--disable-background-networking',
    '--allow-file-access-from-files', '--remote-debugging-port=0',
    '--user-data-dir=' + profile, 'about:blank'
  ], {stdio: ['ignore', 'ignore', 'pipe']});
  let startupError;
  let diagnostics = '';
  child.on('error', error => {startupError = error;});
  child.stderr.on('data', data => {diagnostics = (diagnostics + data).slice(-4000);});
  let ws;
  try {
    let port;
    for (let i = 0; i < 600; i++) {
      if (startupError) throw startupError;
      if (child.exitCode !== null || child.signalCode !== null) break;
      try {port = (await fs.readFile(path.join(profile, 'DevToolsActivePort'), 'utf8')).split('\n')[0]; break;}
      catch {await delay(50);}
    }
    if (!port) throw Error('Chromium debugging endpoint did not start: ' + diagnostics);
    const targets = await (await fetch('http://127.0.0.1:' + port + '/json/list')).json();
    ws = new WebSocket(targets.find(t => t.type === 'page').webSocketDebuggerUrl);
    await new Promise((resolve, reject) => {ws.once('open', resolve); ws.once('error', reject);});
    let serial = 0;
    const waiting = new Map();
    ws.on('message', raw => {
      const m = JSON.parse(raw);
      if (m.id && waiting.has(m.id)) {
        const {resolve, reject, timer} = waiting.get(m.id);
        clearTimeout(timer); waiting.delete(m.id);
        m.error ? reject(Error(JSON.stringify(m.error))) : resolve(m.result);
      }
    });
    const send = (method, params={}) => new Promise((resolve, reject) => {
      const id = ++serial;
      const timer = setTimeout(() => {waiting.delete(id); reject(Error('CDP timeout: ' + method));}, 10000);
      waiting.set(id, {resolve, reject, timer}); ws.send(JSON.stringify({id, method, params}));
    });
    await send('Page.enable');
    const built = await fs.readdir(path.join(root, '_build'));
    const chapters = built.filter(n => /^\d\d-.*\.html$/.test(n));
    if (chapters.length !== 10) throw Error('Expected ten built weekly chapters');
    const pages = [...chapters.sort(),'introduction.html','notation.html','reading-guide.html','attribution.html','epilogue.html'];
    const results = [];
    for (const [mode, width, fontScale] of [['desktop',1440,1],['narrow',390,1],['text-zoom-200',1440,2]]) {
      await send('Emulation.setDeviceMetricsOverride', {width,height:1000,deviceScaleFactor:1,mobile:false});
      for (const file of pages) {
        await send('Page.navigate',{url:pathToFileURL(path.join(root,'_build',file)).href});
        await delay(100);
        const expr = '(async()=>{await document.fonts.ready; if(' + fontScale + '!==1){document.documentElement.style.fontSize=(parseFloat(getComputedStyle(document.documentElement).fontSize)*' + fontScale + ')+"px";} await Promise.all([...document.images].map(i=>i.complete?null:new Promise(r=>{i.onload=r;i.onerror=r})));return {title:document.querySelector("main h1")?.textContent,overflow:document.documentElement.scrollWidth>innerWidth+2,brokenImages:[...document.images].filter(i=>!i.naturalWidth).length,bodyWidth:document.documentElement.scrollWidth,width:innerWidth,mainFont:getComputedStyle(document.querySelector("main")).fontSize}})()';
        const r = await send('Runtime.evaluate',{expression:expr,awaitPromise:true,returnByValue:true});
        if(r.exceptionDetails) throw Error(JSON.stringify(r.exceptionDetails));
        const v = r.result.value;
        results.push({mode,file,...v});
        const screenshot = async suffix => {
          const capture=await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});
          await fs.writeFile(path.join(tmp,mode+'-'+file+'-'+suffix+'.png'),Buffer.from(capture.data,'base64'));
        };
        await screenshot('opening');
        // Capture teaching content as well as page openings for manual QA.
        const count = await send('Runtime.evaluate',{expression:'document.querySelectorAll("main img, main pre, main table").length',returnByValue:true});
        for (let i=0; i<count.result.value; i++) {
          await send('Runtime.evaluate',{expression:'document.querySelectorAll("main img, main pre, main table")['+i+'].scrollIntoView({block:"center"})'});
          await screenshot('content-'+i);
        }
      }
    }
    const failures=results.filter(r=>!r.title||r.overflow||r.brokenImages);
    // Render every original figure at a legible size for label inspection.
    const figures = (await fs.readdir(path.join(root,'_build','figures'))).filter(n=>n.endsWith('.svg')).sort();
    const sheet = path.join(tmp,'figures.html');
    await fs.writeFile(sheet,'<!doctype html><meta charset="utf-8"><style>body{margin:20px;font:20px sans-serif}section{break-inside:avoid}img{width:800px;height:auto}</style>'+figures.map(n=>'<section><h2>'+n+'</h2><img src="'+pathToFileURL(path.join(root,'_build','figures',n)).href+'"></section>').join(''));
    await send('Emulation.setDeviceMetricsOverride',{width:840,height:1000,deviceScaleFactor:1,mobile:false});
    await send('Page.navigate',{url:pathToFileURL(sheet).href});
    await delay(100);
    await send('Runtime.evaluate',{expression:'Promise.all([...document.images].map(i=>i.decode()))',awaitPromise:true});
    const layout = await send('Page.getLayoutMetrics');
    const capture = await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:true,clip:{x:0,y:0,width:840,height:layout.cssContentSize.height,scale:1}});
    await fs.writeFile(path.join(tmp,'figures.png'),Buffer.from(capture.data,'base64'));
    const report = {checked:results.length,failures,screenshots:tmp,figures,results};
    await fs.writeFile(path.join(tmp,'report.json'),JSON.stringify(report,null,2));
    console.log(JSON.stringify(report,null,2));
    if(failures.length) process.exitCode=1;
  } finally {
    ws?.close(); child.kill('SIGTERM');
  }
})().catch(e=>{console.error(e);process.exitCode=1;});
