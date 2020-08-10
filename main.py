from Graph_Builder import GraphBuilder
from Heap import Heap
import random

heap_test_array = [4, 9, 12, 9, 4, 13, 4, 8, 11]
random.shuffle(heap_test_array)
heap = Heap(heap_test_array)
heap.insert(2)


source_dir = "graphs"
graph_source = "matrix_8_vertexes_16_edges_dijkstra_algorithm.csv"
graph = GraphBuilder(is_oriented=True).build_from_matrix("{}/{}".format(source_dir, graph_source))
routes = dict(graph.dijkstra_recursive(set(range(8)), 0))
print(routes)

