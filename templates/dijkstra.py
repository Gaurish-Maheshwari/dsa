import heapq

def dijkstra(graph, src):
    n = len(graph)
    dist = [float('inf')] * n
    dist[src] = 0

    pq = [(0, src)]   # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, wt in graph[u]:
            if d + wt < dist[v]:
                dist[v] = d + wt
                heapq.heappush(pq, (dist[v], v))

    return dist
