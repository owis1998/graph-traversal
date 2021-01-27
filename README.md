# graph-traversal

graph traversal refers to the process of visiting each vertex in a graph.
note that any argument pass to the algorithm function should be a list of vertices and dic represents adjacency list, like this:

vertices_list = ['B', 'C', 'D', 'E', 'F', 'G', 'H']
adj_list = {
			 'B' : [('C', 8), ('F', 7), ('H', 9)],
			 'C' : [('D', 1), ('E', 2), ('F', 4), ('B', 8)],
			 'D' : [('C', 1), ('E', 4)],
			 'E' : [('C', 2), ('D', 4), ('G', 3)],
			 'G' : [('E', 3), ('F', 1), ('H', 5)],
			 'H' : [('B', 9), ('G', 5)],
			 'F' : [('C', 4), ('B', 7), ('G', 1)]
			}
