def BFS(start, graph):
    level = {start: 0}
    parent = {start: None}
    i = 1
    frontier = [start]
    while frontier:
        next = []
        for u in frontier:
            for v in graph[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next  
        i += 1
        
        
    
    return parent

def DFS(graph):
    parent = {}
    for vertex in graph:
        if vertex not in parent:
            parent[vertex] = None
            DFS_helper(vertex,graph, parent)
            
    return parent

def DFS_helper(start, graph, parent):
    for vertex in graph[start]:
        if vertex not in parent:
            parent[vertex] = start
            DFS_helper(vertex,graph, parent)
    