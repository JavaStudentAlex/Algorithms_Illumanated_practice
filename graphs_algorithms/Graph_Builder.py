import numpy as np
from numpy import genfromtxt
from graphs_algorithms.Adjacency_List_Graph import AdjacencyListGraph
from graphs_algorithms.Adjacency_Matrix_Graph import AdjacencyMatrixGraph


class GraphBuilder:

    missing = -1

    def __init__(self, is_oriented=False):
        self.oriented = is_oriented

    def build_from_matrix(self, matrix_source_file):
        adjacency_matrix = genfromtxt(fname=matrix_source_file, dtype='int', delimiter=',', filling_values=self.missing)
        nodes = adjacency_matrix.shape[0]

        overall_connections = len(adjacency_matrix[adjacency_matrix != self.missing])
        edges = overall_connections // 2 if self.oriented else overall_connections
        return AdjacencyListGraph(self.__make_adjacency_list(adjacency_matrix)) \
            if self.__is_sparse(nodes, edges) else AdjacencyMatrixGraph(adjacency_matrix)

    @staticmethod
    def __is_sparse(nodes, edges):
        estimated_nodes_number = pow(nodes, 2)
        edges_diff = (edges - estimated_nodes_number) / edges
        if edges_diff > -0.05:
            return False
        return True

    def __make_adjacency_list(self, matrix):
        result_adjacency_list = []

        def making_adjacency_nodes(row):
            adjacency_nodes = {adjacency_node: row[adjacency_node] for adjacency_node in
                               np.where(row != self.missing)[0]}
            result_adjacency_list.append(adjacency_nodes)

        np.apply_along_axis(making_adjacency_nodes, 1, matrix)

        return result_adjacency_list

    def build_from_list(self, list_source_file):
        data_for_adjacency_list = genfromtxt(fname=list_source_file, dtype="int", delimiter=' ')

        nodes = len(np.unique(data_for_adjacency_list))
        edges = len(data_for_adjacency_list)
        result_adjacency_list = [dict() for node in range(nodes)]

        def insert_data_into_adjacency_list(row):
            result_adjacency_list[row[0]-1][row[1]-1] = 1

        np.apply_along_axis(insert_data_into_adjacency_list, 1, data_for_adjacency_list)
        return AdjacencyListGraph(result_adjacency_list) if self.__is_sparse(nodes, edges) \
            else AdjacencyMatrixGraph(self.__make_adjacency_matrix(result_adjacency_list))

    def __make_adjacency_matrix(self, adjacency_list):
        nodes = len(adjacency_list)
        result_adjacency_matrix = np.full(dtype="int", fill_value=self.missing, shape=(nodes, nodes))

        for node in range(nodes):
            adjacency_nodes_dict = adjacency_list[node]
            for next_node, edge_val in adjacency_nodes_dict.items():
                result_adjacency_matrix[node][next_node] = edge_val
        return result_adjacency_matrix





