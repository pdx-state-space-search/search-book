#!/usr/bin/env python3
"""Render the original Week 1 growth illustration.

Requires matplotlib. Curves use total nodes through a regular tree's
specified depth; this is an illustrative model, not experimental data.
"""
from pathlib import Path
import xml.etree.ElementTree as ET

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / 'src/figures/search-growth.svg'
BUDGET = 1_000_000


def total_nodes(branching, depth):
    """Return the geometric-series total, allowing interpolated depths."""
    return (branching ** (depth + 1) - 1) / (branching - 1)


with plt.rc_context({'font.family': 'DejaVu Sans',
                     'font.size': 13, 'svg.fonttype': 'none',
                     'svg.hashsalt': 'search-book-growth'}):
    fig, ax = plt.subplots(figsize=(9, 5.1))
    fig.subplots_adjust(left=.20, right=.96, bottom=.17, top=.83)
    depths = [i / 40 for i in range(801)]
    for branching, color in ((4, '#a34b13'), (2, '#17628c')):
        ax.plot(depths, [total_nodes(branching, d) for d in depths],
                color=color, linewidth=3,
                label=f'{branching} children per node')
    ax.axhline(BUDGET, color='#38434e', linestyle='--', linewidth=1.5)
    ax.text(.5, BUDGET + 60_000, 'Illustrative budget: 1 million nodes',
            color='#38434e', fontsize=12)
    for branching, depth, color in ((4, 9, '#a34b13'), (2, 18, '#17628c')):
        work = total_nodes(branching, depth)
        ax.plot(depth, work, 'o', color=color, markersize=7)
        ax.annotate(f'Depth {depth} fits', (depth, work),
                    xytext=(depth - 3.5, work + 180_000),
                    fontsize=12, color=color,
                    arrowprops={'arrowstyle': '-', 'color': color})
    ax.set(xlim=(0, 20), ylim=(0, 1_650_000),
           xlabel='Search depth (decisions)', ylabel='Total search nodes')
    ax.set_xticks(range(0, 21, 2))
    ax.set_yticks([0, 500_000, 1_000_000, 1_500_000])
    ax.yaxis.set_major_formatter(FuncFormatter(
        lambda value, _: '0' if value == 0 else f'{value / 1_000_000:g} million'))
    ax.grid(axis='y', color='#dce1e5', linewidth=.8)
    ax.set_axisbelow(True)
    ax.spines[['top', 'right']].set_visible(False)
    ax.legend(loc='upper left', frameon=False, fontsize=12)
    fig.suptitle('Less branching extends the useful range',
                 fontsize=17, fontweight='bold', y=.97)
    fig.text(.5, .89, 'Both curves continue above the plotted range.',
             ha='center', fontsize=12, color='#38434e')
    fig.savefig(TARGET, format='svg', bbox_inches='tight', metadata={
        'Date': None, 'Creator': 'ChatGPT, State-Space Search course book'})
    plt.close(fig)

namespace = 'http://www.w3.org/2000/svg'
ET.register_namespace('', namespace)
tree = ET.parse(TARGET)
svg = tree.getroot()
svg.set('role', 'img')
svg.set('aria-labelledby', 'growth-title growth-desc')
title = ET.Element(f'{{{namespace}}}title', {'id': 'growth-title'})
title.text = 'Reducing branching moves a fixed search budget to greater depth'
desc = ET.Element(f'{{{namespace}}}desc', {'id': 'growth-desc'})
desc.text = ('Total nodes through depth d are (b^(d+1)-1)/(b-1). '
             'The four-child tree fits a million-node budget through depth 9, '
             'but exceeds it at depth 10. The two-child tree fits through '
             'depth 18, but exceeds the budget at depth 19. Both grow beyond '
             'the vertical plotting range. This is a mathematical illustration.')
svg.insert(0, title)
svg.insert(1, desc)
tree.write(TARGET, encoding='utf-8', xml_declaration=True)
print(TARGET)
