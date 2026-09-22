import heapq

GRAPH = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 5, 'E': 2},
    'C': {'E': 1},
    'D': {'F': 3},
    'E': {'D': 1, 'F': 6},
    'F': {}
}

HEURISTICS = {
    'A': 7,
    'B': 5,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 0
}


def a_star_search(graph, heuristics, start_node, goal_node):
    open_list = [(0 + heuristics[start_node], start_node)]
    g_cost = {node: float("inf") for node in graph}
    g_cost[start_node] = 0
    came_from = {}

    while open_list:
        popped_element = heapq.heappop(open_list)
        f_cost, current_node = popped_element

        if current_node == goal_node:
            path = reconstruct_path(came_from, current_node)
            cost = g_cost[current_node]
            return path, cost

        for neighbour, travel_cost in graph[current_node].items():
            tentative_g = g_cost[current_node] + travel_cost

            if tentative_g < g_cost[neighbour]:
                g_cost[neighbour] = tentative_g
                came_from[neighbour] = current_node

                h = heuristics.get(neighbour, float("inf"))
                new_f = tentative_g + h

                heapq.heappush(open_list, (new_f, neighbour))

    return None, 0


def reconstruct_path(came_from, current_node):
    path = [current_node]

    while current_node in came_from:
        current_node = came_from[current_node]
        path.append(current_node)

    return path[::-1]


if __name__ == "__main__":
    START = 'A'
    GOAL = 'F'

    path, cost = a_star_search(GRAPH, HEURISTICS, START, GOAL)

    print(f"Path is {path}")
    print(f"Cost is {cost}")