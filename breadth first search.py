def algorithm(graph):
	visited_vertices = []
	visited = []
	def fn(vertices):
		if not vertices.peekFirst() in visited_vertices:
			visited_vertices.append(vertices.peekFirst())

		for ver in vertices.getAll():
			if not ver in visited_vertices:
				visited_vertices.append(ver)

		visited.append(vertices.peekFirst())
		for ver in vertices.getAll():
			if not ver in visited:
				fn(graph.find(ver))

	fn(graph.get_first())
	return visited_vertices
