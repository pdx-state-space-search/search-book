#!/usr/bin/env python3
"""Finite checks for memory-bounded and bidirectional search.
Reference values come from Floyd-Warshall, not either search.
"""
import heapq
import itertools
import math
from check_algorithms import all_pairs


def rbfs(n, edges, h):
    adj = [[] for _ in range(n)]
    for u,v,c in edges:
        adj[u].append((v,c))
    def visit(s,g,f,limit,path):
        if s == n-1:
            return g,f
        children = [[max(f,g+c+h[t]),t,g+c] for t,c in adj[s]
                    if t not in path]
        if not children:
            return None,math.inf
        while True:
            children.sort()
            best=children[0]
            if math.isinf(best[0]) or best[0] > limit:
                return None,best[0]
            alternative=children[1][0] if len(children)>1 else math.inf
            answer,backed=visit(best[1],best[2],best[0],
                               min(limit,alternative),path|{best[1]})
            best[0]=backed
            if answer is not None:
                return answer,backed
    result,_ = visit(0,0,h[0],math.inf,{0})
    return math.inf if result is None else result


def bidirectional(n,edges):
    forward=[[] for _ in range(n)]
    backward=[[] for _ in range(n)]
    for u,v,c in edges:
        forward[u].append((v,c))
        backward[v].append((u,c))
    adj=[forward,backward]
    distances=[{0:0},{n-1:0}]
    queues=[[(0,0)],[(0,n-1)]]
    mu=math.inf
    while True:
        for side in (0,1):
            while queues[side] and queues[side][0][0] != distances[side][queues[side][0][1]]:
                heapq.heappop(queues[side])
        if not queues[0] or not queues[1]:
            return mu
        if queues[0][0][0]+queues[1][0][0] >= mu:
            return mu
        side=0 if queues[0][0][0] <= queues[1][0][0] else 1
        d,u=heapq.heappop(queues[side])
        if u in distances[1-side]:
            mu=min(mu,d+distances[1-side][u])
        for v,c in adj[side][u]:
            proposal=d+c
            if proposal < distances[side].get(v,math.inf):
                distances[side][v]=proposal
                heapq.heappush(queues[side],(proposal,v))
            if v in distances[1-side]:
                mu=min(mu,proposal+distances[1-side][v])


pairs=[(u,v) for u in range(3) for v in range(3) if u != v]
bidirectional_count=0
rbfs_count=0
for costs in itertools.product((None,0,1,3),repeat=6):
    edges=[(u,v,c) for (u,v),c in zip(pairs,costs) if c is not None]
    d=all_pairs(3,edges)
    assert bidirectional(3,edges) == d[0][2], edges
    bidirectional_count+=1
    if any(c == 0 for _,_,c in edges):
        continue
    ranges=[range(min(4,int(d[s][2]) if math.isfinite(d[s][2]) else 4)+1)
            for s in (0,1)]
    for first,second in itertools.product(*ranges):
        h=[first,second,0]
        assert rbfs(3,edges,h) == d[0][2], (edges,h)
        rbfs_count+=1

print(f'PASS: bidirectional Dijkstra on {bidirectional_count:,} directed graphs')
print(f'PASS: RBFS on {rbfs_count:,} positive-cost graph/heuristic cases')
print('These are finite regression checks, not general proofs.')
