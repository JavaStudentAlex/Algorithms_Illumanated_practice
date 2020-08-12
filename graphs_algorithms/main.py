from graphs_algorithms.Graph_Builder import GraphBuilder


source_dir = "graphs"
graph_source = "matrix_8_vertexes_16_edges_dijkstra_algorithm.csv"
graph = GraphBuilder(is_oriented=True).build_from_matrix("{}/{}".format(source_dir, graph_source))
routes = dict(graph.dijkstra_recursive(set(range(8)), 0))
print(routes)

