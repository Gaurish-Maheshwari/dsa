def bellman_ford(n, edges, src):
    INF = float('inf')
    dist = [INF] * n
    dist[src] = 0

    # Relax all edges n-1 times
    for _ in range(n - 1):
        changed = False

        for u, v, wt in edges:
            if dist[u] != INF and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt
                changed = True

        if not changed:
            break

    # Check for negative cycle
    for u, v, wt in edges:
        if dist[u] != INF and dist[u] + wt < dist[v]:
            return None   # negative cycle exists

    return dist
