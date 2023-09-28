def make_union_find(V):
    parent = [-1] * V
    rank = [0] * V
    return parent, rank

def find(vertex, parent):
    if parent[vertex] == -1:
        return vertex
    parent[vertex] = find(parent[vertex], parent)  # Path compression
    return parent[vertex]

def union(src, dest, parent, rank):
    root1 = find(src, parent)
    root2 = find(dest, parent)

    if root1 != root2:
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root2] = root1
            rank[root1] += 1

def kruskal(graph):
    edges = []
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            if (neighbor, vertex, weight) not in edges:
                edges.append((vertex, neighbor, weight))
    
    edges.sort(key=lambda edge: edge[2])

    V = len(graph)
    parent, rank = make_union_find(V)

    mst = []

    for edge in edges:
        src, dest, weight = edge
        if find(src, parent) != find(dest, parent):
            mst.append(edge)
            union(src, dest, parent, rank)

    return mst

# Given graph
graph = {
    0: [(1,10),(4,5),(3,10)],
    1: [(0,10),(2,9)],
    2: [(1,9),(3,10),(6,9)],
    3: [(0,10),(2,10),(4,10),(6,10)],
    4: [(0,5),(3,10),(7,10)],
    5: [(7,10)],
    6: [(2,9),(3,10),(7,9)],
    7: [(4,10),(5,10),(6,9)]
}

# Perform kruskal's algorithm
mst = kruskal(graph)

print("Edges in the minimum spanning tree:")
for edge in mst:
    print(f"({edge[0]}, {edge[1]}) -> {edge[2]}")
