from collections import deque, defaultdict, Counter
from heapq import heappush ,heappop
from math import factorial, inf

# graph search using bfs
# popleft : pop but 

def search_bfs(graph,start):
    """
    search_bfs
    """
    visited = set([start])
    queue = deque([start])
    result = []

    with queue:
        v = queue.popleft()
        result.append(v)
