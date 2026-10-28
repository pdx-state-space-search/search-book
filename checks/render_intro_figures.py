#!/usr/bin/env python3
"""Write original SVG diagrams for the recurring introductory examples.

The graph-coloring picture also serves as the Chapter 2 constraint graph.
All geometry and teaching labels are local to this book.
"""
from html import escape
from pathlib import Path

FIGURES = Path(__file__).resolve().parents[1] / 'src/figures'


def text(x, y, value, size=22, anchor='middle', weight='normal'):
    """Return an escaped, consistently styled SVG text element."""
    return (f'<text x="{x}" y="{y}" font-size="{size}" '
            f'text-anchor="{anchor}" font-weight="{weight}">'
            f'{escape(str(value))}</text>')


def write(name, title, description, height, drawing):
    """Write an accessible, self-contained original diagram."""
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" '
           f'viewBox="0 0 840 {height}" role="img" '
           'aria-labelledby="title desc">'
           f'<title id="title">{escape(title)}</title>'
           f'<desc id="desc">{escape(description)}</desc>'
           f'<rect width="840" height="{height}" fill="white"/>'
           '<g font-family="sans-serif" fill="#17212b">'
           + drawing + '</g></svg>\n')
    (FIGURES / name).write_text(svg)
    print(FIGURES / name)


positions = {'A': (160, 130), 'B': (160, 330),
             'C': (440, 230), 'D': (700, 230)}
colors = {'A': '#f6cbd0', 'B': '#cee8d4',
          'C': '#cde3f5', 'D': '#f6cbd0'}
parts = [text(420, 38, 'Graph coloring', 26, weight='bold')]
for u, v in (('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D')):
    x1, y1 = positions[u]
    x2, y2 = positions[v]
    parts.append(f'<path d="M{x1} {y1}L{x2} {y2}" '
                 'stroke="#33475b" stroke-width="3"/>')
for label, (x, y) in positions.items():
    parts.append(f'<circle cx="{x}" cy="{y}" r="33" '
                 f'fill="{colors[label]}" stroke="#33475b" stroke-width="2"/>')
    parts.append(text(x, y + 8, label, 26))
parts += [text(110, 137, 'red', anchor='end'),
          text(110, 337, 'green', anchor='end'),
          text(440, 175, 'blue'), text(700, 292, 'red'),
          text(420, 420, 'Each edge requires different colors.', 21)]
write('graph-coloring.svg', 'A feasible graph coloring',
      'Edges AB, AC, BC, and CD require different endpoint colors. '
      'A is red, B green, C blue, and D red. There is no edge AD.',
      450, ''.join(parts))

parts = [text(420, 38, 'Number partitioning', 26, weight='bold')]
for top, title, groups in (
        (95, 'Candidate 1: imbalance 4', ((8, 5, 4), (7, 6))),
        (290, 'Candidate 2: imbalance 0', ((6, 5, 4), (7, 8)))):
    parts.append(text(420, top - 20, title, 22))
    for left, label, weights in ((40, 'A', groups[0]), (460, 'B', groups[1])):
        parts.append(f'<rect x="{left}" y="{top}" width="340" height="120" '
                     'rx="10" fill="#f1f6fb" stroke="#33475b" stroke-width="2"/>')
        parts.append(text(left + 25, top + 42, label, 24))
        for i, weight in enumerate(weights):
            x = left + 70 + i * 76
            parts.append(f'<rect x="{x}" y="{top + 15}" width="62" height="42" '
                         'rx="6" fill="#d5e7f4" stroke="#42647f"/>')
            parts.append(text(x + 31, top + 44, weight, 24))
        parts.append(text(left + 170, top + 98, f'Sum = {sum(weights)}', 22))
parts.append(text(420, 455, 'Each candidate uses every weight exactly once.', 20))
write('number-partitioning.svg', 'Two partitions and their objective values',
      'Weights 8, 5, 4 versus 7, 6 have sums 17 and 13, imbalance 4. '
      'Weights 6, 5, 4 versus 7, 8 have sums 15 and 15, imbalance zero.',
      480, ''.join(parts))

parts = [
    '<defs><marker id="gray-arrow" markerWidth="10" markerHeight="10" '
    'refX="8" refY="4" orient="auto" markerUnits="userSpaceOnUse">'
    '<path d="M0 0L8 4L0 8Z" fill="#596774"/></marker>'
    '<marker id="green-arrow" markerWidth="12" markerHeight="12" '
    'refX="10" refY="5" orient="auto" markerUnits="userSpaceOnUse">'
    '<path d="M0 0L10 5L0 10Z" fill="#28744c"/></marker></defs>',
    text(420, 38, 'Pathfinding', 26, weight='bold'),
    '<path d="M134 140L706 140" stroke="#596774" stroke-width="3" '
    'marker-end="url(#gray-arrow)"/>',
    '<path d="M130 157L390 299" fill="none" '
    'stroke="#28744c" stroke-width="4" marker-end="url(#green-arrow)"/>',
    '<path d="M450 299L710 157" fill="none" '
    'stroke="#28744c" stroke-width="4" marker-end="url(#green-arrow)"/>',
    text(420, 115, '20', 24), text(240, 240, '1', 24), text(600, 240, '1', 24)]
for name, x, y in (('S', 100, 140), ('A', 420, 315), ('G', 740, 140)):
    parts.append(f'<circle cx="{x}" cy="{y}" r="33" fill="#dceaf7" '
                 'stroke="#33475b" stroke-width="2"/>')
    parts.append(text(x, y + 8, name, 26))
parts.append(text(420, 408, 'S → G costs 20.  S → A → G costs 2.', 23))
write('pathfinding.svg', 'Path cost and number of edges differ',
      'S has a directed edge to G costing 20. S to A and A to G '
      'each cost 1. The two-edge path costs 2 and is highlighted in green.',
      440, ''.join(parts))
