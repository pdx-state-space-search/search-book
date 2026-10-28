#!/usr/bin/env python3
"""Independent finite checks for the editorial review, not course code.

Exhaustive small models catch implementation and exposition mistakes;
these checks are not proofs of general theorems. Only the Python standard
library is required. Keep this file outside mdBook's student-facing src/.
"""
import heapq
import itertools
import math


def all_pairs(n, edges):
    d = [[math.inf] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for a, b, c in edges:
        d[a][b] = min(d[a][b], c)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def best_first(n, edges, h, weight=1):
    adj = [[] for _ in range(n)]
    for a, b, c in edges:
        adj[a].append((b, c))
    g = [math.inf] * n
    g[0] = 0
    q = [(weight * h[0], 0, 0)]
    while q:
        _, old_g, s = heapq.heappop(q)
        if old_g != g[s]:
            continue
        if s == n - 1:
            return old_g
        for t, cost in adj[s]:
            candidate = old_g + cost
            if candidate < g[t]:
                g[t] = candidate
                heapq.heappush(q, (candidate + weight * h[t], candidate, t))
    return math.inf


def ida(n, edges, h):
    adj = [[] for _ in range(n)]
    for a, b, c in edges:
        adj[a].append((b, c))
    threshold = h[0]
    def visit(s, g, path):
        f = g + h[s]
        if f > threshold:
            return False, f
        if s == n - 1:
            return True, g
        exceeded = math.inf
        for t, cost in adj[s]:
            if t in path:
                continue
            found, result = visit(t, g + cost, path | {t})
            if found:
                return True, result
            exceeded = min(exceeded, result)
        return False, exceeded
    while threshold < math.inf:
        found, result = visit(0, 0, {0})
        if found:
            return result
        threshold = result
    return math.inf


def check_path_search():
    count = 0
    vertices = 3
    pairs = [(a, b) for a in range(vertices) for b in range(vertices) if a != b]
    # Every directed three-vertex graph with absent, zero, one or three costs.
    for choices in itertools.product((None, 0, 1, 3), repeat=len(pairs)):
        edges = [(a, b, c) for (a, b), c in zip(pairs, choices) if c is not None]
        d = all_pairs(vertices, edges)
        if not math.isfinite(d[0][-1]):
            assert best_first(vertices, edges, [0] * vertices) == math.inf
            continue
        # Every integer admissible heuristic in a bounded finite range,
        # including inconsistent choices. Dead ends have unrestricted h*.
        ranges = [range(min(6, int(d[s][-1]) if math.isfinite(d[s][-1]) else 6) + 1)
                  for s in range(vertices - 1)] + [range(1)]
        for h in itertools.product(*ranges):
            assert best_first(vertices, edges, h) == d[0][-1], (edges, h)
            for weight in (1.5, 2, 3):
                got = best_first(vertices, edges, h, weight)
                assert got <= weight * d[0][-1], (edges, h, weight, got)
            if all(c > 0 for _, _, c in edges):
                assert ida(vertices, edges, h) == d[0][-1], (edges, h)
            count += 1
    # Classic reopening case: A is expanded via cost 3, then improved to 2.
    edges = [(0, 1, 3), (0, 2, 1), (2, 1, 1), (1, 3, 3)]
    assert best_first(4, edges, [5, 0, 4, 0]) == 5
    # A generated goal of cost 10 cannot justify stopping before cost 2.
    assert best_first(3, [(0, 2, 10), (0, 1, 1), (1, 2, 1)], [0, 0, 0]) == 2
    return count


def ac3(domains, relations):
    ds = [set(x) for x in domains]
    neighbors = {v: set() for v in range(len(ds))}
    for a, b in relations:
        neighbors[a].add(b)
    queue = list(relations)
    while queue:
        a, b = queue.pop(0)
        old = ds[a].copy()
        ds[a] = {x for x in ds[a] if any((x, y) in relations[a, b] for y in ds[b])}
        if ds[a] != old:
            if not ds[a]:
                return ds
            queue += [(k, a) for k in neighbors[a] if k != b]
    return ds


def check_constraints():
    pairs = list(itertools.product(range(2), repeat=2))
    relations = [set(p for i, p in enumerate(pairs) if mask & (1 << i))
                 for mask in range(16)]
    count = 0
    for rs in itertools.product(relations, repeat=3):
        arcs = {}
        for (a, b), allowed in zip(((0, 1), (0, 2), (1, 2)), rs):
            arcs[a, b] = allowed
            arcs[b, a] = {(y, x) for x, y in allowed}
        solutions = [a for a in itertools.product(range(2), repeat=3)
                     if all((a[x], a[y]) in r for (x, y), r in arcs.items())]
        reduced = ac3([range(2)] * 3, arcs)
        assert all(all(a[v] in reduced[v] for v in range(3)) for a in solutions)
        if all(reduced):
            for (a, b), r in arcs.items():
                assert all(any((x, y) in r for y in reduced[b]) for x in reduced[a])
        count += 1
    # Arc consistency does not decide satisfiability: 2-color a triangle.
    neq = {(0, 1), (1, 0)}
    arcs = {(a, b): neq for a in range(3) for b in range(3) if a != b}
    assert all(ac3([range(2)] * 3, arcs))
    assert not any(all(a[x] != a[y] for x in range(3) for y in range(x))
                   for a in itertools.product(range(2), repeat=3))
    return count


def minimax(leaves, maximizing=True):
    if len(leaves) == 1:
        return leaves[0]
    mid = len(leaves) // 2
    values = (minimax(leaves[:mid], not maximizing), minimax(leaves[mid:], not maximizing))
    return (max if maximizing else min)(values)


def alphabeta(leaves, maximizing=True, alpha=-math.inf, beta=math.inf):
    if len(leaves) == 1:
        return leaves[0]
    mid = len(leaves) // 2
    value = -math.inf if maximizing else math.inf
    for child in (leaves[:mid], leaves[mid:]):
        got = alphabeta(child, not maximizing, alpha, beta)
        if maximizing:
            value = max(value, got)
            alpha = max(alpha, value)
        else:
            value = min(value, got)
            beta = min(beta, value)
        if alpha >= beta:
            break
    return value


def check_games():
    count = 0
    for leaves in itertools.product((-1, 0, 1), repeat=8):
        assert alphabeta(leaves) == minimax(leaves)
        count += 1
    return count


def check_local_math():
    count = 0
    for weights in itertools.product((1, 2, 3), repeat=4):
        for signs in itertools.product((-1, 1), repeat=4):
            difference = sum(w * s for w, s in zip(weights, signs))
            for i in range(4):
                changed = list(signs)
                changed[i] *= -1
                actual = abs(sum(w * s for w, s in zip(weights, changed)))
                assert actual == abs(difference - 2 * signs[i] * weights[i])
                count += 1
    assert math.isclose(math.exp(-4 / 2), 0.1353352832366127)
    # Geometric independent restarts, cost t paid per trial (including success).
    p, t = .25, 10
    finite_sum = sum(k * t * ((1 - p) ** (k - 1)) * p for k in range(1, 1000))
    assert math.isclose(finite_sum, t / p)
    return count


if __name__ == '__main__':
    checks = {
        'admissible path-search cases (A*, weighted A*, positive-cost IDA*)': check_path_search(),
        'binary constraint networks (solution preservation and fixed point)': check_constraints(),
        'depth-three zero-sum game trees (alpha-beta versus minimax)': check_games(),
        'partition-move delta cases and stochastic arithmetic': check_local_math(),
    }
    for name, count in checks.items():
        print(f'PASS: {count:,} {name}')
    print('Finite checks passed. These are regression evidence, not general proofs.')
