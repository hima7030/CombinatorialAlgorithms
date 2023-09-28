def bfs_traversal(adj_matrix, start_vertex):
    n = len(adj_matrix)
    visited = [False] * n
    queue = [(start_vertex, None)]  # Each element is a tuple (vertex, parent)
    bfs_matrix = [[0 for _ in range(n)] for _ in range(n)]

    while queue:
        current, parent = queue.pop(0)
        if not visited[current]:
            visited[current] = True
            if parent is not None:
                bfs_matrix[current][parent] = 1  
            for i in range(n):
                if adj_matrix[current][i] == 1 and not visited[i]:
                    queue.append((i, current))

    return bfs_matrix

# Input adjacency matrix
graph_matrix = [
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0]
]

# Perform BFS traversal starting from vertex 0 (A)
bfs_result_matrix = bfs_traversal(graph_matrix, 0)

# Print the BFS traversal matrix
vertices = ['A', 'B', 'C', 'D', 'E']
print('  ', ' '.join(vertices))
for i, row in enumerate(bfs_result_matrix):
    print(vertices[i], ' '.join(map(str, row)))
