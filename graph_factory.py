import random

import networkx as nx

from edge_thresholds_graph_with_terminals import EdgeThresholdsGraphWithTerminals

random.seed(6)


def create_edge_thresholds_graph_with_terminals():
    G = nx.Graph()

    nodes = map(str, range(1, 6))
    terminals = nodes[::2]

    for i, n1 in enumerate(nodes[:-1]):
        for n2 in nodes[i + 1:]:
            if n1 != n2:
                G.add_edge(n1, n2, tu=random.randint(1, 10), tv=random.randint(1, 10))

    return EdgeThresholdsGraphWithTerminals(G, terminals)
