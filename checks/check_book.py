#!/usr/bin/env python3
"""Check the mdBook source contract and generated internal hyperlinks."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'
BUILD = ROOT / '_build'
errors = []
warnings = []
chapters = sorted(SRC.glob('[0-9][0-9]-*.md'))
if len(chapters) != 10:
    errors.append(f'Expected ten chapters, found {len(chapters)}')
for label, name in re.findall(r'^- \[([^\]]+)\]\((\d\d-[^)]+\.md)\)',
                              (SRC / 'SUMMARY.md').read_text(), re.M):
    headings = re.findall(r'^# (.+)$', (SRC / name).read_text(), re.M)
    title = re.sub(r'^Week \d+:\s*', '', headings[0]) if headings else ''
    if label != title:
        errors.append(f'{name}: contents label {label!r} differs from title {title!r}')
words = {}
for chapter in chapters:
    text = chapter.read_text()
    words[chapter.name] = len(re.findall(r"\b[\w’'-]+\b", text))
    if words[chapter.name] > 3500:
        warnings.append(f'{chapter.name}: {words[chapter.name]} words exceeds target')
    if words[chapter.name] < 2000:
        warnings.append(f'{chapter.name}: only {words[chapter.name]} words; assess depth')
    if re.search(r'^#{1,6}\s+.*\b(exercises?|homework|answer key|exercise solutions)\b', text, re.I | re.M):
        errors.append(f'{chapter.name}: forbidden exercise/solution section')
    for language in re.findall(r'^\x60\x60\x60([^\n]*)', text, re.M):
        if language.strip().lower() not in ('', 'text', 'plaintext', 'pseudocode'):
            errors.append(f'{chapter.name}: unexpected source-language fence {language!r}')
    if re.search(r'||turn\d+(?:search|view)\d+', text):
        errors.append(f'{chapter.name}: unresolved chat-only citation marker')
    if re.search(r'\b(TODO|TBD|FIXME|INSERT HERE)\b', text):
        errors.append(f'{chapter.name}: unresolved placeholder')
    if re.search(r'(?<!\\)\$\$|\\\(|\\\[', text):
        warnings.append(f'{chapter.name}: potential unrendered LaTeX')
    for alt, image in re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', text):
        if not alt.strip():
            errors.append(f'{chapter.name}: image lacks alt text')
        if not (SRC / image).is_file():
            errors.append(f'{chapter.name}: missing image {image}')

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        for key in ('href', 'src'):
            if key in a:
                self.links.append(a[key])

pages = {}
for path in BUILD.rglob('*.html'):
    page = Page()
    page.feed(path.read_text())
    pages[path.resolve()] = page
if not pages:
    errors.append('No generated HTML found; run mdbook build first')
links_checked = 0
for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc or link.startswith('data:'):
            continue
        if not url.path:
            target = path
        elif url.path.startswith('/'):
            target = (BUILD / unquote(url.path.lstrip('/'))).resolve()
        else:
            target = (path.parent / unquote(url.path)).resolve()
        if target.is_dir():
            target /= 'index.html'
        if not target.exists():
            errors.append(f'{path.name}: missing target {link}')
        elif url.fragment and target in pages:
            if unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{path.name}: missing anchor {link}')
        links_checked += 1
report = {'weekly_word_counts': words, 'html_pages': len(pages),
          'internal_links_checked': links_checked, 'errors': errors,
          'warnings': warnings}
print(json.dumps(report, indent=2))
raise SystemExit(bool(errors))
