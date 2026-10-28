# Desktop interruption investigation

Checked 2026-10-22 Pacific. No application settings changed.

## Evidence

- Crashpad sidecar at 2026-10-22T07:06:59.943Z
  (00:06:59 Pacific) records capture_kind=crash, ptype=browser.
  No minidump or stack trace found in pending/new/completed.
- Project .chatgpt-install/launch.log from earlier launch records
  nouveau/DRI3 failure, invalid EGL visual, GPU initialization
  failure, and renderer zygote fork/broken-pipe errors.
  These do not establish the cause of the later browser crash.
- App logs at ~/.local/state/codex/logs/2026/10/22/ show
  executor read_error at 06:59:19Z, expired HTTP 401 at
  06:59:20Z, and recovered connection at 06:59:24Z.
  Five-second interruption, not evidence of permanent outage.
- Shell tool fails before command execution: bwrap cannot
  mount proc on /proc (Operation not permitted).
- Node runtime filesystem and child-process access succeeds;
  mdBook v0.5.2 and independent algorithm checks ran there.
- Current main process command title includes --disable-gpu.
- System journal access is limited; coredumpctl unavailable.

## Conclusions and mitigation

Main-process crash confirmed by marker; root cause unresolved.
Graphics failures and sandbox failures are distinct evidence.
Do not attribute all transport closures to GPU or credentials.
Save drafts directly and frequently. Keep work/status on disk;
never treat agent final responses as durable chapter storage.
A client-independent worker is a future architectural option,
not a fix applied in this campaign.
