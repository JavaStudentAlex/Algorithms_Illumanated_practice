from graphs_algorithms.Graph_Abstract import GraphAbstract


class AdjacencyMatrixGraph(GraphAbstract):

    def __init__(self, matrix):
        super().__init__(matrix)
