import heapq

def a_star(graph, heuristic, start, goal):
    open_list = [(0, start)]
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    parent = {node: None for node in graph}

    while open_list:
        current_f, current = heapq.heappop(open_list)

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path, g_cost[goal]

        for neighbor, cost in graph[current]:
            new_g_cost = g_cost[current] + cost

            if new_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_g_cost
                parent[neighbor] = current
                f_cost = new_g_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))

    return None, float('inf')


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1), ('E', 3)],
    'E': [('D', 3)]
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}

start = 'A'
goal = 'E'

path, cost = a_star(graph, heuristic, start, goal)

if path:
    print("Optimal Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")