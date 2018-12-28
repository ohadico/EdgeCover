import networkx as nx
import matplotlib.pyplot as plt
from typing import Iterable, Dict, Tuple


class EdgeThresholdsGraph(nx.Graph):
    def __init__(self, terminals, thresholds, **attr):
        """
        :param terminals: list of nodes that are terminals
        :type terminals: Iterable[str]
        :param thresholds: mapping from edge to 2 thresholds
        :type thresholds: Dict[Tuple[str, str], Tuple[float, float]]
        """
        super(EdgeThresholdsGraph, self).__init__(**attr)
        self._terminals = set(terminals)
        self._thresholds = thresholds
        self.add_edges_from(self.get_edges_sorted())
        self._is_bipartite = None

    def get_terminals(self):
        return self._terminals

    def get_nonterminals(self):
        return self.nodes - self._terminals

    def get_edges_sorted(self):
        return self._thresholds.keys()

    def get_thresholds(self):
        return self._thresholds.items()

    def get_thresholds_at(self, e):
        return self._thresholds[e]

    @staticmethod
    def sort_position(terminals_pos, axis=1):
        return dict(zip(sorted(terminals_pos.keys(), reverse=True),
                        sorted(terminals_pos.values(), key=lambda p: p[axis])))

    def is_bipartite(self):
        if self._is_bipartite is not None:
            return self._is_bipartite

        terminals = self.get_terminals()
        nonterminals = self.get_nonterminals()
        for e in self.edges.keys():
            if e[0] in terminals and e[1] in terminals or e[0] in nonterminals and e[1] in nonterminals:
                self._is_bipartite = False
                break
        else:
            self._is_bipartite =  True

        return self._is_bipartite

    def get_layout(self, seed=0):
        if self.is_bipartite():
            pos = nx.bipartite_layout(self, self.get_terminals())

            # sort position
            terminals_pos = {n: p for n, p in pos.items() if n in self.get_terminals()}
            pos.update(self.sort_position(terminals_pos, 1))  # sort by y axis
            nonterminals_pos = {n: p for n, p in pos.items() if n not in self.get_terminals()}
            pos.update(self.sort_position(nonterminals_pos, 1))
        else:
            pos = nx.spring_layout(self, seed=seed)

        return pos

    def draw(self, node_labels=None, terminal_color='r', nonterminal_color='w',
             tu=0.1, tv=0.9, save=None):
        pos = self.get_layout()

        nodes_drawing = nx.draw_networkx_nodes(self, pos, nodelist=self.get_terminals(),
                                               node_color=terminal_color)
        nodes_drawing.set_edgecolor('black')
        nodes_drawing = nx.draw_networkx_nodes(self, pos, nodelist=self.get_nonterminals(),
                                               node_color=nonterminal_color)
        nodes_drawing.set_edgecolor('black')

        if node_labels is not None:
            nx.draw_networkx_labels(self, pos, labels=node_labels)

        nx.draw_networkx_edges(self, pos)

        self._draw_thresholds(pos, tu, tv)

        plt.axis('off')

        if save is not None:
            plt.savefig(save)

        plt.show()

    def _draw_thresholds(self, pos, tu, tv):
        edge_labels = {e: t[0] for e, t in self.get_thresholds()}
        self._draw_edge_labels(pos, edge_labels, tu)
        edge_labels = {e: t[1] for e, t in self.get_thresholds()}
        self._draw_edge_labels(pos, edge_labels, tv)

    def _draw_edge_labels(self, pos, edge_labels, loc=0.5):
        nx.draw_networkx_edge_labels(self, pos,
                                     edge_labels=edge_labels,
                                     label_pos=loc,
                                     rotate=False)
