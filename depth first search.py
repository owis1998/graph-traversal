visited_vertices = []

def algorihm(vertex, adj_list):
	def fn(vertex, adj_list):
		visited_vertices.append(vertex)
		
		for ver in adj_list[vertex]:
			if not ver in visited_vertices:
				fn(ver, adj_list)

	fn(vertex, adj_list)
	return visited_vertices
