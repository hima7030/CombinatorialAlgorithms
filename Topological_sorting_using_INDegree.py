from collections import deque

def topological_sort(graph):
    # Number of vertices
    V = len(graph)
    
    # Create a dictionary to keep track of in-degrees of vertices
    in_degree = {}
    
    # Initialize in-degrees to 0 for all vertices
    for i in graph:
        in_degree[i] = 0
    
    # Update in-degrees based on the graph
    for i in graph:
        for j in graph[i]:
            in_degree[j] += 1
    
    # Create a queue to store all vertices with in-degree 0
    queue = deque()
    for i in in_degree:
        if in_degree[i] == 0:
            queue.append(i)
    #print(queue)

    # List to store the topological order
    top_order = []
    
    # Process until the queue is empty
    while queue:
        # Get the next vertex from the queue
        u = queue.popleft()
        top_order.append(u)
        
        # Reduce in-degree of all adjacent vertices
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # Check if the topological order has all vertices
    if len(top_order) != V:
        return "The graph has a cycle, so topological sorting is not possible."
    else:
        return top_order

# Given graph
graph = {0:[3,4,6] , 1:[2,4,5] , 2:[3] , 3:[4] , 4:[5,6] , 5:[6] , 6:[]}

# Perform topological sort
result = topological_sort(graph)
map_alpha = {i: f'V{i+1}' for i in range(len(graph))}
print(f"Topological sorting:{[map_alpha[i] for i in result]}")
