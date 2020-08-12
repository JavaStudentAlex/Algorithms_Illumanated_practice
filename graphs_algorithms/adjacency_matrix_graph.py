from graphs_algorithms.graph_abstract import GraphAbstract


class AdjacencyMatrixGraph(GraphAbstract):

    def __init__(self, matrix):
        super().__init__(matrix)
