from graphs_algorithms.graph_builder import GraphBuilder


source_dir = "graphs"
file_name = "small_graph_for_spanning_tree.txt"

graph = GraphBuilder().build_from_weighted_list("{}/{}".format(source_dir, file_name))
best_spanning_tree = graph.find_best_spanning_tree_prima()
print(best_spanning_tree)
