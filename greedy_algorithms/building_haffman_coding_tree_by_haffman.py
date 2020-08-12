from greedy_algorithms.haffman_tree import HaffmanTree
from graphs_algorithms.heap import Heap


def cover_by_nodes(freq_iter):
    yield from ((freq, HaffmanTree(None, None, frequency=freq)) for freq in freq_iter)


def build_haffman_tree(freq_iter):
    freq_nodes_iter = cover_by_nodes(freq_iter)
    source_nodes = Heap(freq_nodes_iter)

    while source_nodes.get_size() >= 2:
        _, min_elem = source_nodes.pop_min()
        _, second_min = source_nodes.pop_min()
        joined_nodes = HaffmanTree(min_elem, second_min)
        source_nodes.insert((joined_nodes.get_overall_frequency(), joined_nodes))
    freq, tree = source_nodes.pop_min()
    return tree
