from collections import defaultdict

import networkx as nx

from graphs.edge_thresholds import EdgeThresholdsGraph


class EdgeThresholdsMultiGraph(EdgeThresholdsGraph, nx.MultiGraph):
    def _draw_thresholds(self, pos, tu, tv, rotate):
        edge_labels = defaultdict(list)
        for e, t in self.get_thresholds():
            edge_labels[e[:2]].append("{}:{}".format(*t))
        for e, l in edge_labels.items():
            edge_labels[e] = '\n'.join(l)
        nx.draw_networkx_edge_labels(self, pos, edge_labels=edge_labels, rotate=rotate)
