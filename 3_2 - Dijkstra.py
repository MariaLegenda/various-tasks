
# поиск кратчайшего пути по алгоритму Дейкстры

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

# start - вершина с которой надо начать 
def dijkstra(graph, start):

	lenght = len(graph)
	is_visited = [False] * lenght
	# стоимость пути до вершины. пока - бесконечность
	cost = [float('inf')] * lenght
	parent = [-1] * lenght

	cost[start] = 0
	min_cost = 0

	while min_cost < float('inf'):

		is_visited[start] = True

		for i, vertex in enumerate(graph[start]):
			if vertex != 0 and not is_visited[i]:

				# обход смежных вершин и запись расстояний до них
				if cost[i] > vertex + cost[start]:
					cost[i] = vertex + cost[start]
					parent[i] = start

		min_cost = float('inf')
		for i in range(lenght):
			if min_cost > cost[i] and not is_visited[i]:
				min_cost = cost[i]
				start = i

	# список вершин, которые необходимо обойти
	ways = []
	for i in range(lenght):
		j = i
		way = [i]
		while parent[j] != -1:
			way.append(parent[j])
			j = parent[j]
		ways.append(way)

	return cost, ways


s = int(input('От какой вершины идти: '))

result = dijkstra(g, s)

print(f'Стоимость путей до каждой вершины {result[0]}')
print(f'Списки вершин дo каждой вершины {result[1]}')

