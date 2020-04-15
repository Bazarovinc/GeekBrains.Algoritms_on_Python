"""3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все
    вершины связаны, по алгоритму поиска в глубину (Depth-First Search)."""

import random


def dfs(graph, start, path=[]):
    path += [start]
    for i in range(len(graph[start])):
        if i not in path and graph[start][i] != 0:
            path = dfs(graph, i, path)
    return path


def make_graph(n):
    graph = []
    for _ in range(n):
        line = []
        for _ in range(n):
            line.append(random.randint(0, 1))
        graph.append(line)
    return graph


n = int(input("Введите размер графа: "))
graph = make_graph(n)
print("Полученный граф: ")
for i in graph:
    print(i)
start = int(input("От какой вершины идти: "))
print(dfs(graph, start))
