import networkx as nx
from typing import List, Dict


class EdgeThresholdsGraphWithTerminals(object):
    def __init__(self, G, terminals):
        """
        :type G: nx.Graph
        :param terminals: list of nodes that are terminals
        :type terminals: List[str]
        """
        self._graph = G
        self._terminals = set(terminals)

    def get_graph(self):
        return self._graph

    def get_nodes(self):
        return set(self._graph.nodes)

    def get_terminals(self):
        return self._terminals

    def get_layout(self, seed=0):
        return nx.spring_layout(self.get_graph(), seed=seed)
