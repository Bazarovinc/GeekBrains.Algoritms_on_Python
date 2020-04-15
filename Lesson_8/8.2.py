"""2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
    которые необходимо обойти."""

from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    start1 = start
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    ways = []
    for n in range(length):
        if n == start:
            ways.append(deque([start, n]))
        else:
            ways.append(deque([start]))
    parent = [-1] * length
    cost[start] = 0
    min_cost = 0
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    for i in range(length):
        if i == start1:
            ways[i] = []
        elif cost[i] == float('inf'):
            ways[i] = [-1]
        else:
            j = i
            while parent[j] != start1:
                if start1 in ways[i]:
                    ways[i] = deque([i])
                    ways[i].appendleft(parent[j])
                else:
                    ways[i].appendleft(parent[j])
                j = parent[j]
            if start1 not in ways[i]:
                ways[i].appendleft(start1)
            elif i not in ways[i]:
                ways[i].append(i)
    return cost, ways


start = int(input("Введите стартовую вершину: "))
cost, ways = dijkstra(g, start)
for i in range(len(ways)):
    if i == start:
        print(f"Из этой {i} вершины начинается путь")
    elif -1 in ways[i] and cost[i] == float('inf'):
        print(f"К {i} вершине нет пути")
    else:
        print(f"Путь {ways[i]} имеет длину {cost[i]}")
