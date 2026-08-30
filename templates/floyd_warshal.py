def floyd_warshall(n, edges):
    INF = float('inf')

    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, wt in edges:
        dist[u][v] = wt

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j])

    return dist
