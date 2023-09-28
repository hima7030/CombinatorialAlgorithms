import collections

def bfs(graph, root):
    visited = []
    queue = collections.deque([(root, None)])  # Each element is a tuple (vertex, parent)

    while queue:
        print("queue:", [i[0] for i in queue])
        vertex, parent = queue.popleft()
        
        if vertex not in visited:
            visited.append(vertex)
            if parent is not None:
                print(f"Traversed edge: ({parent}, {vertex})")
            print("visited:", visited)
            
            for neighbor in graph[vertex]:
                if neighbor not in visited and neighbor not in [i[0] for i in queue]:
                    queue.append((neighbor, vertex))
    
    return visited

if __name__ == "__main__":
    graph = { 0:[1,3,4], 1:[0,2], 2:[1,4], 3:[0], 4:[1,2,0] }
    final_visited = bfs(graph, 0)
    map_alpha = {0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E'}
    print(f"BFS is: {[map_alpha[i] for i in final_visited]}")
