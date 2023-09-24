
def topological_sort_dfs(graph):
    # Number of vertices
    V = len(graph)
    
    # Create a set to keep track of visited vertices
    visited = set()
    
    # Stack to store the topological order
    stack = []
    
    # Recursive DFS function
    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(v)
    
    # Call DFS for each unvisited vertex
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
    
    # The stack now contains the topological order
    return stack[::-1]  # Reverse the stack to get the order

# Given graph
graph = {0:[3,4,6] , 1:[2,4,5] , 2:[3] , 3:[4] , 4:[5,6] , 5:[6] , 6:[]}

# Perform topological sort using DFS
result = topological_sort_dfs(graph)
print(result)
