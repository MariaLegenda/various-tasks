
# поиск кратчайшего пути в ширину. 
# неориентированный, невзвеш граф

from collections import deque

g = [
	[0, 1, 1, 0, 1, 0, 0, 0],
	[1, 0, 0, 0, 0, 0, 0, 0],
	[1, 0, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 1, 0, 0],
	[1, 0, 1, 0, 0, 0, 1, 0],
	[0, 0, 0, 1, 0, 0, 1, 1],
	[0, 0, 0, 0, 1, 1, 0, 1],
	[0, 0, 0, 0, 0, 1, 1, 0],
]

#start - вершина с которой надо начать, finifsh - вершина в которую прийти  
def bfs(graph, start, finish):
	#родитель для каждой вершины
	parent = [None for _ in range(len(graph))]
	# визит. Если были в этой вершине - True, если нет False. 
	## is_ - если хрантся логические данные
	is_visited = [False for _ in range(len(graph))]
	# очередь начинается со старта
	deq = deque([start])
	is_visited[start] = True

	while len(deq) > 0:
		curent = deq.pop()
		if curent == finish:
			# return parent
			break

		# просмотреть вершины, которые связаны с текущей
		for i, vertex in enumerate(graph[curent]):
			# == 1 - т.е. следующая(смежная) и ее не посещали
			if vertex == 1 and not is_visited[i]:

				is_visited[i] = True
				# добавляем в список parent из какой вершины пришли
				parent[i] = curent
				deq.appendleft(i)	

	else:
		return f'Из вершины  {start} нельзя попасть в вершину {finish}'

	# вывести наикратчайший путь
	cost = 0 # стоимость пути
	way = deque([finish]) # добавить в очередь целевую вершину
	i = finish # значение целевой вершины

	while parent[i] != start:
		cost += 1
		way.appendleft(parent[i])
		i = parent[i]

	cost +=1
	way.appendleft(start)

	return f'кратчайший путь {list(way)} длиной в {cost} у.е.'


s = int(input('start: '))
f = int(input('finish: '))

print(bfs(g, s, f))