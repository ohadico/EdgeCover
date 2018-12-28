import networkx as nx
import matplotlib.pyplot as plt
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
        self._thresholds = thresholds
        self._is_bipartite = None

    def get_graph(self):
        return self._graph

    def get_nodes(self):
        return set(self._graph.nodes)

    def get_terminals(self):
        return self._terminals

    @staticmethod
    def sort_position(terminals_pos, axis=1):
        return dict(zip(sorted(terminals_pos.keys(), reverse=True),
                        sorted(terminals_pos.values(), key=lambda p: p[axis])))

    def is_bipartite(self):
        if self._is_bipartite is not None:
            return self._is_bipartite

        terminals = self.get_terminals()
        nonterminals = self.get_nodes() - self.get_terminals()

        for e in self.get_graph().edges.keys():
            if e[0] in terminals and e[1] in terminals or e[0] in nonterminals and e[1] in nonterminals:
                self._is_bipartite = False
                break
        else:
            self._is_bipartite =  True

        return self._is_bipartite

    def get_layout(self, seed=0):
        if self.is_bipartite():
            pos = nx.bipartite_layout(self.get_graph(), self.get_terminals())

            # sort position
            terminals_pos = {n: p for n, p in pos.items() if n in self.get_terminals()}
            pos.update(self.sort_position(terminals_pos, 1))  # sort by y axis
            nonterminals_pos = {n: p for n, p in pos.items() if n not in self.get_terminals()}
            pos.update(self.sort_position(nonterminals_pos, 1))
        else:
            pos = nx.spring_layout(self.get_graph(), seed=seed)

        return pos

    def draw(self, node_labels=None, terminal_color='r', nonterminal_color='w', save=None):
        G = self.get_graph()
        pos = self.get_layout()

        nodes_drawing = nx.draw_networkx_nodes(G, pos, nodelist=self.get_terminals(),
                                               node_color=terminal_color)
        nodes_drawing.set_edgecolor('black')
        nodes_drawing = nx.draw_networkx_nodes(G, pos, nodelist=self.get_nodes() - self.get_terminals(),
                                               node_color=nonterminal_color)
        nodes_drawing.set_edgecolor('black')

        if node_labels is not None:
            nx.draw_networkx_labels(G, pos, labels=node_labels)

        nx.draw_networkx_edges(G, pos)

        edge_labels = {e: t[0] for e, t in self._thresholds.items()}
        nx.draw_networkx_edge_labels(G, pos,
                                     edge_labels=edge_labels,
                                     label_pos=0.1,
                                     rotate=False)

        label_pos = 0.9 if not self.is_bipartite() else 0.8
        edge_labels = {e: t[1] for e, t in self._thresholds.items()}
        nx.draw_networkx_edge_labels(G, pos,
                                     edge_labels=edge_labels,
                                     label_pos=label_pos,
                                     rotate=False)

        plt.axis('off')

        if save is not None:
            plt.savefig(save)

        plt.show()

