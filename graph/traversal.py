#coding:utf-8
from collections import deque
def some_graph():
    a, b, c, d, e, f, g, h = range(8)
    N = [
        [b, c, d, e, f],    # a
        [c, e],             # b
        [d],                # c
        [e],                # d
        [f],                # e
        [c, g, h],          # f
        [f, h],             # g
        [f, g]              # h
    ]
    return N

def some_tree():
    a, b, c, d, e, f, g, h = range(8)
    N = [
        [b, c],             # a
        [d, e],             # b
        [f, g],             # c
        [],                 # d
        [],                 # e
        [],                 # f
        [h],                # g
        []                  # h
    ]
    return N

class stack(list):
    add = list.append

G = some_graph()
def traversal(G,s):
    Visited,Q = set(),set()
    Q.add(s)
    while Q:
        element = Q.pop()
        if element in Visited:
            continue
        Visited.add(element)
        for v in G[element]:
            Q.add(v)
        yield element

#print(list(traversal(G,0)))


def rec_dfs(G, s, S=None):
    if S is None: S = set()                     # Initialize the history
    S.add(s)                                    # We've visited s
    for u in G[s]:                              # Explore neighbors
        if u in S: continue                     # Already visited: Skip
        rec_dfs(G, u, S)                        # New: Explore recursively
    return S # For testing


def iter_dfs(G, s):
    S, Q = set(), []                            # Visited-set and queue
    Q.append(s)                                 # We plan on visiting s
    while Q:                                    # Planned nodes left?
        u = Q.pop()                             # Get one
        if u in S: continue                     # Already visited? Skip it
        S.add(u)                                # We've visited it now
        Q.extend(G[u])                          # Schedule all neighbors
        yield u                                 # Report u as visited

print(list(iter_dfs(G,0)))

def bfs(G, s):
    P, Q = {s: None}, deque([s])                # Parents and FIFO queue
    while Q:
        u = Q.popleft()                         # Constant-time for deque
        for v in G[u]:
            if v in P: continue                 # Already has parent
            P[v] = u                            # Reached from u: u is parent
            Q.append(v)
    return P

print(bfs(G,0))

























































