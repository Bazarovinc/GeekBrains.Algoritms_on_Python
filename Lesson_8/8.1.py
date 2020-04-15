"""1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
    Сколько рукопожатий было?"""

n = int(input("Введите колличество друзей: "))
graph = []
for i in range(n):
    line = []
    for j in range(n):
        if j == i:
            line.append(0)
        else:
            line.append(1)
    graph.append(line)
handshakes = 0
i = 0
while i < len(graph):
    j = i
    while j < len(graph):
        if graph[i][j] == 1:
            handshakes += 1
        j += 1
    i += 1
print(f"Среди {n}-и друзей было {handshakes} рукопожатий")
