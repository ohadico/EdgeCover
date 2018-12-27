import networkx as nx
from typing import List, Dict, Tuple


class EdgeThresholdsGraphWithTerminals(object):
    def __init__(self, G, terminals, thresholds):
        """
        :type G: nx.Graph
        :param terminals: list of nodes that are terminals
        :type terminals: List[str]
        :param thresholds: mapping from edge to 2 thresholds
        :type thresholds: Dict[Tuple[str, str], Tuple[float, float]]
        """
        self._graph = G
        self._terminals = set(terminals)
        self._thresholds = set(thresholds)

    def get_graph(self):
        return self._graph

    def get_nodes(self):
        return set(self._graph.nodes)

    def get_terminals(self):
        return self._terminals

    def get_layout(self, seed=0):
        return nx.spring_layout(self.get_graph(), seed=seed)
