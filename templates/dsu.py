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
        return

    if size[a] < size[b]:
        a, b = b, a

    parent[b] = a
    size[a] += size[b]

def same(a, b):
    return find(a) == find(b)
