def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])

    parent = list(range(n))
    size = [1] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a == b:
            return False

        if size[a] < size[b]:
            a, b = b, a

        parent[b] = a
        size[a] += size[b]

        return True

    ans = 0

    for u, v, wt in edges:
        if union(u, v):
            ans += wt

    return ans
