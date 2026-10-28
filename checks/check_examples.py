#!/usr/bin/env python3
"""Independently enumerate small examples used in the book.
These checks concern named finite examples, not general proofs.
"""
from collections import deque
from itertools import product
from math import exp, log, isclose

# Week 1: check the new introductory candidates by enumeration.
color_edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
colorings = list(product(('red', 'green', 'blue'), repeat=4))
def proper_coloring(colors):
    return all(colors[u] != colors[v] for u, v in color_edges)
assert len(colorings) == 81
assert proper_coloring(('red', 'green', 'blue', 'red'))
assert not any(proper_coloring(c) for c in colorings
               if c[0] == c[1] == 'red')
weights = (8, 7, 6, 5, 4)
assert min(abs(sum(w * sign for w, sign in zip(weights, signs)))
           for signs in product((-1, 1), repeat=5)) == 0

# Sum the actual integer layers independently of the plotted formula.
node_counts = {d: sum(2**i for i in range(d + 1))
               for d in (20, 30, 40)}
assert list(node_counts.values()) == [2_097_151, 2_147_483_647,
                                      2_199_023_255_551]
assert 3**20 == 3_486_784_401
assert round(node_counts[20] / 1_000_000, 1) == 2.1
assert round(node_counts[30] / 1_000_000 / 60, 1) == 35.8
assert round(node_counts[40] / 1_000_000 / 86_400, 1) == 25.5
for branching, last_depth in ((4, 9), (2, 18)):
    assert sum(branching**i for i in range(last_depth + 1)) <= 1_000_000
    assert sum(branching**i for i in range(last_depth + 2)) > 1_000_000
assert 19 < log(1_000_000, 2) < 20

# Week 2: SAT two-color triangle; inspect all Boolean assignments.
triangle = [(0, 1), (1, 2), (2, 0)]
for assignment in product((False, True), repeat=3):
    cnf = all((assignment[u] or assignment[v]) and
              (not assignment[u] or not assignment[v])
              for u, v in triangle)
    coloring = all(assignment[u] != assignment[v] for u, v in triangle)
    assert cnf == coloring
    assert not cnf

# Week 2: reproduce the stated AC-3 queue discipline and trace.
domains = {v: set((1, 2, 3)) for v in 'XYZ'}
neighbors = {'X': ['Y'], 'Y': ['X', 'Z'], 'Z': ['Y']}
def allowed(u, a, v, b):
    return a < b if (u, v) in [('X', 'Y'), ('Y', 'Z')] else b < a
queue = deque([('X', 'Y'), ('Y', 'X'), ('Y', 'Z'), ('Z', 'Y')])
trace = []
while queue:
    u, v = queue.popleft()
    removed = {a for a in domains[u]
               if not any(allowed(u, a, v, b) for b in domains[v])}
    domains[u] -= removed
    trace.append((u + v, tuple(sorted(removed))))
    assert domains[u]
    if removed:
        for z in neighbors[u]:
            if z != v and (z, u) not in queue:
                queue.append((z, u))
assert trace == [('XY', (3,)), ('YX', (1,)), ('YZ', (3,)),
                 ('ZY', (1, 2)), ('XY', (2,))], trace
assert domains == {'X': {1}, 'Y': {2}, 'Z': {3}}

# Week 6: recoloring trace and all single-item neighbors.
edges = [(0,1),(0,2),(1,2),(2,3)]
def conflicts(colors):
    return sum(colors[u] == colors[v] for u,v in edges)
assert [conflicts(c) for c in [('r','r','r','r'),
        ('r','r','b','r'),('g','r','b','r')]] == [4,1,0]
A, B = (8,5,4), (7,6)
assert abs(sum(A)-sum(B)) == 4
scores = [abs(sum(A)-2*w-sum(B)) for w in A]
scores += [abs(sum(A)+2*w-sum(B)) for w in B]
assert scores == [12,6,4,18,16]
assert sum((6,5,4)) == sum((7,8)) == 15

# Week 7: acceptance and independent restart model.
assert isclose(exp(-4/2), 0.1353352832366127)
assert isclose(-4/log(.8), 17.925680470898204)
assert isclose(1-.8**5, .67232)
assert isclose((1-.2)/.2*20+30, 110)
assert isclose((17-8)-(13+8), -12)
assert abs((17-8+6)-(13+8-6)) == 0

# Week 8: exhaustively solve original and delete-relaxed courier.
# Facts: AtA, AtB, HasKey, Carrying, Delivered.
actions = [({0},{2},set()), ({0,2},{1},{0}),
           ({1,3},{4},{3}), ({1,2},{0},{1})]
def courier(relaxed):
    start = frozenset((0,3))
    q = deque([(start, 0)])
    seen = {start}
    while q:
        state, distance = q.popleft()
        if {0,4} <= state:
            return distance
        for pre, add, delete in actions:
            if pre <= state:
                nxt = frozenset((set(state) - (set() if relaxed else delete)) | add)
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, distance+1))
assert courier(False) == 4
assert courier(True) == 3

# Exhaust all integer schedules with makespan <= 7 and two machines.
durations = (3,2,4,2)
best = float('inf')
feasible = 0
for starts in product(range(8), repeat=4):
    ends = tuple(s+d for s,d in zip(starts,durations))
    if ends[0] > starts[2] or ends[1] > starts[3] or max(ends) > 7:
        continue
    for machines in product((0,1), repeat=4):
        if any(machines[i] == machines[j] and
               starts[i] < ends[j] and starts[j] < ends[i]
               for i in range(4) for j in range(i+1,4)):
            continue
        feasible += 1
        best = min(best,max(ends))
assert best == 7 and feasible > 0
assert 35_200_000/2**20 > 33.5 and 35_200_000/2**20 < 33.6
print('PASS: introductory coloring/partition candidates and growth/budget arithmetic')
print('PASS: SAT encoding, AC-3 trace, local repair/partition examples')
print('PASS: annealing and independent-restart arithmetic')
print('PASS: courier optimum 4 vs relaxed 3; schedule optimum 7')
print('These finite examples do not establish general algorithm guarantees.')
