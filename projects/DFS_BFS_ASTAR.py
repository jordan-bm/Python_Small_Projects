# Jordan Burmylo-Magrann
# File: BFS_DFS_ASTAR.py
# Program: Implement BFS, DFS, and ASTAR graph search algorithms on Romania map


# Imports
from collections import deque
import heapq

# Romania Map Graph (with distances)
romania_map ={
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Dobreta', 120), ('Pitesti', 138), ('Rimnicu Vilcea', 146)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

# Straight-line distances (heuristics) to Bucharest
heuristic = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161,
    'Fagaras': 178, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 98, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

# Depth-First Search
def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, _ in romania_map[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None

# Breadth-First Search
def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor, _ in romania_map[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# A* Search
def astar(start, goal):
    pq = [(heuristic[start], 0, start, [start])] # f, g, node, path
    visited = {}
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node == goal:
            return path
        if node in visited and visited[node] <= g:
            continue
        visited[node] = g
        for neighbor, cost in romania_map[node]:
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))
    return None

# Run calls
print('DFS path:', dfs('Arad', 'Bucharest'))
print('BFS path:', bfs('Arad', 'Bucharest'))
print('A* path:', astar('Arad', 'Bucharest'))

    
