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

# Week 2: ground the three finite clause families independently, then
# compare all satisfying truth assignments with direct graph colorings.
def coloring_clauses(n, k, graph):
    """Expand the three finite clause families from the text."""
    clauses = [[((v, c), True) for c in range(k)] for v in range(n)]
    clauses += [[((v, c), False), ((v, d), False)]
                for v in range(n) for c in range(k) for d in range(c + 1, k)]
    clauses += [[((u, c), False), ((v, c), False)]
                for u, v in graph for c in range(k)]
    return clauses


ground_cases = 0
possible_edges = [(0, 1), (0, 2), (1, 2)]
instances = [(3, k, [edge for i, edge in enumerate(possible_edges)
                    if mask & (1 << i)]) for k in (1, 2, 3) for mask in range(8)]
instances.append((4, 3, color_edges))
for n, k, graph in instances:
    names = [(v, c) for v in range(n) for c in range(k)]
    clauses = coloring_clauses(n, k, graph)
    decoded = set()
    for bits in product((False, True), repeat=len(names)):
        values = dict(zip(names, bits))
        if all(any(values[name] == positive for name, positive in clause)
               for clause in clauses):
            assert all(sum(values[v, c] for c in range(k)) == 1
                       for v in range(n))
            decoded.add(tuple(next(c for c in range(k) if values[v, c])
                              for v in range(n)))
        ground_cases += 1
    direct = {colors for colors in product(range(k), repeat=n)
              if all(colors[u] != colors[v] for u, v in graph)}
    assert decoded == direct, (n, k, graph)
    if n == 4:
        assert len(names) == 12 and len(clauses) == 28 and len(decoded) == 12

# Week 2: forward-checking domains follow the displayed assignment trace.
domains = {v: set(('red', 'green', 'blue')) for v in 'ABCD'}
assigned = {}
color_edges_named = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D')]
for variable, value, expected in (
        ('A', 'red', {'B': {'green', 'blue'}, 'C': {'green', 'blue'},
                      'D': {'red', 'green', 'blue'}}),
        ('B', 'green', {'B': {'green'}, 'C': {'blue'},
                        'D': {'red', 'green', 'blue'}}),
        ('C', 'blue', {'B': {'green'}, 'C': {'blue'}, 'D': {'red', 'green'}})):
    assigned[variable] = value
    domains[variable] = {value}
    for u, v in color_edges_named:
        if u == variable and v not in assigned:
            domains[v].discard(value)
        if v == variable and u not in assigned:
            domains[u].discard(value)
    assert {v: domains[v] for v in 'BCD'} == expected

# Week 2 unit propagation and Week 6 SAT repair use the same formula.
def sat_score(p, q, r):
    return sum(not clause for clause in (p or q, not p or r, not q))
assert [values for values in product((False, True), repeat=3)
        if sat_score(*values) == 0] == [(True, False, True)]
assert [sat_score(*values) for values in ((False, False, False),
        (True, False, False), (True, False, True))] == [1, 1, 0]

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
print(f'PASS: {ground_cases:,} grounded SAT assignments; forward-checking trace')
print('PASS: SAT unit/repair examples, local repair, and partition examples')
print('PASS: annealing and independent-restart arithmetic')
print('PASS: courier optimum 4 vs relaxed 3; schedule optimum 7')
print('These finite examples do not establish general algorithm guarantees.')
