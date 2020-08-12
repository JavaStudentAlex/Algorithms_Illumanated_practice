from graphs_algorithms.graph_abstract import GraphAbstract


class AdjacencyListGraph(GraphAbstract):

    def __init__(self, adjacency_list):
        super().__init__(adjacency_list)

    def bfs(self, node_number):
        found_nodes = {node_number}
        next_nodes = [node_number]

        while len(next_nodes) != 0:
            border_node = next_nodes.pop(0)

            undiscovered_nodes = set(self.graph[border_node].keys()).difference(found_nodes)

            found_nodes.update(undiscovered_nodes)
            next_nodes.extend(undiscovered_nodes)
        yield from found_nodes

    def dfs(self, node_number, found_nodes=None):
        found_nodes = set() if found_nodes is None else found_nodes
        found_nodes.add(node_number)
        next_nodes = [node_number]

        while len(next_nodes) != 0:
            deep_border_node = next_nodes.pop()

            deep_undiscovered_nodes = set(self.graph[deep_border_node].keys()).difference(found_nodes)

            found_nodes.update(deep_undiscovered_nodes)
            next_nodes.extend(deep_undiscovered_nodes)
            yield deep_border_node

    def recursive_dfs(self, node_number, found_nodes=None):
        found_nodes = set() if found_nodes is None else found_nodes
        found_nodes.add(node_number)

        reverse_ordered_nodes = list()

        deep_undiscovered_nodes = set(self.graph[node_number].keys()).difference(found_nodes)
        found_nodes.update(deep_undiscovered_nodes)

        yield node_number
        for next_deep_node in deep_undiscovered_nodes:
            reverse_ordered_nodes = list(self.recursive_dfs(next_deep_node, found_nodes)) + reverse_ordered_nodes
        yield from reverse_ordered_nodes

    def best_route_bfs(self, node_number):
        found_nodes = {node_number: 0}
        next_nodes = [node_number]

        while len(next_nodes) != 0:
            border_node = next_nodes.pop(0)
            border_node_route_cost = found_nodes[border_node]

            for new_node, new_edge_cost in self.graph[border_node].items():
                new_node_route_cost = border_node_route_cost + new_edge_cost

                if new_node not in found_nodes.keys():
                    found_nodes[new_node] = new_node_route_cost
                    next_nodes.append(new_node)
                elif new_node_route_cost < found_nodes[new_node]:
                    found_nodes[new_node] = new_node_route_cost
                    next_nodes.append(new_node)
        yield from found_nodes.items()

    def find_connected_components_bfs(self):
        connected_components = list()
        nodes_to_scout = set(range(len(self.graph)))

        while len(nodes_to_scout) != 0:
            new_node = nodes_to_scout.pop()

            new_connected_component = self.bfs(new_node)
            connected_components.append(new_connected_component)

            nodes_to_scout = nodes_to_scout.difference(new_connected_component)
        yield from connected_components

    def topological_sort_dfs(self):
        sorted_nodes = list()
        all_nodes = set(range(len(self.graph)))

        while len(sorted_nodes) != len(all_nodes):
            next_node_to_start_scout = all_nodes.difference(sorted_nodes).pop()
            next_sorted_nodes = list(self.dfs(next_node_to_start_scout, set(sorted_nodes)))
            sorted_nodes = next_sorted_nodes + sorted_nodes
        yield from sorted_nodes

    def find_highly_connected_components(self):
        reversed_graph = self.build_reversed_graph()
        reversed_topological_sort = list(reversed_graph.topological_sort_dfs())

        found_nodes = set()
        while len(reversed_topological_sort) != 0:
            cur_node = reversed_topological_sort.pop(0)
            highly_connected_component = set(self.dfs(cur_node, found_nodes))

            reversed_topological_sort = [node for node in reversed_topological_sort if node
                                         not in highly_connected_component]
            found_nodes.update(highly_connected_component)
            yield highly_connected_component

    def build_reversed_graph(self):
        all_nodes = range(len(self.graph))
        result_adjacency_nodes = [dict() for node in all_nodes]

        for cur_node in all_nodes:
            adjacency_nodes = self.graph[cur_node]
            for adjacent_node, edge_value in adjacency_nodes.items():
                result_adjacency_nodes[adjacent_node][cur_node] = edge_value
        return AdjacencyListGraph(result_adjacency_nodes)

    def dijkstra_recursive(self, nodes_to_find_seq, next_node_to_add, cost=0, found_nodes=None):

        def scout_node():
            found_nodes[next_node_to_add] = cost
            if next_node_to_add in nodes_to_find_seq:
                nodes_to_find_seq.remove(next_node_to_add)

        def mark_undiscovered_nodes():
            undiscovered_nodes = set(nodes_to_find_seq).difference(found_nodes.keys())
            if len(undiscovered_nodes) != 0:
                found_nodes.update({undisc_node: -1 for undisc_node in undiscovered_nodes})

        if nodes_to_find_seq is not set:
            nodes_to_find_seq = set(nodes_to_find_seq)

        found_nodes = dict() if found_nodes is None else found_nodes
        scout_node()

        if len(nodes_to_find_seq) == 0:
            yield from found_nodes.items()
        else:
            try:
                next_node, next_node_cost = self.__find_best_next_node(found_nodes)
                yield from self.dijkstra_recursive(nodes_to_find_seq, next_node, next_node_cost, found_nodes)
            except IndexError:
                mark_undiscovered_nodes()
                yield from found_nodes.items()

    def __find_best_next_node(self, found_nodes):
        next_nodes_variant = list()

        def fill_next_nodes_variants(current_node):
            node_cost = found_nodes[current_node]

            def fill_next_nodes_for_current_node(next_node):
                edge_cost = self.graph[current_node][next_node]
                next_nodes_variant.append((next_node, node_cost + edge_cost))

            undiscovered_nodes = set(self.graph[current_node]).difference(found_nodes.keys())
            list(map(fill_next_nodes_for_current_node, undiscovered_nodes))

        list(map(fill_next_nodes_variants, found_nodes.keys()))

        if len(next_nodes_variant) == 0:
            raise IndexError

        return min(next_nodes_variant, key=lambda node_cost_pair: node_cost_pair[1])

def find_best_spanning_tree_kraskala():
    pass








