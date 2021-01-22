visited_vertices = []
visited = []

def algorithm(vertex, adj_list):
	def fn(vertex, adj_list):
		if not vertex in visited_vertices:
			visited_vertices.append(vertex)

		for ver in adj_list[vertex]:
			if not ver in visited_vertices:
				visited_vertices.append(ver)

		visited.append(vertex)
		for ver in adj_list[vertex]:
			if not ver in visited:
				fn(ver, adj_list)

	fn(vertex, adj_list)
	return visited_vertices
