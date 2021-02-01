def algorihm(graph):
	visited_vertices = []
	def fn(vertices):
		visited_vertices.append(vertices.peekFirst())
		
		for ver in vertices.getAll():
			if not ver in visited_vertices:
				fn(graph.find(ver))

	fn(graph.get_first())
	return visited_vertices
