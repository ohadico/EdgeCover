import random

import networkx as nx

from edge_thresholds_graph_with_terminals import EdgeThresholdsGraphWithTerminals

random.seed(6)


def create_edge_thresholds_graph_with_terminals():
    G = nx.Graph()

    nodes = map(str, range(1, 6))
    terminals = nodes[::2]
    thresholds = {}

    for i, n1 in enumerate(nodes[:-1]):
        for n2 in nodes[i + 1:]:
            if n1 != n2:
                G.add_edge(n1, n2)
                thresholds[(n1, n2)] = (random.randint(1, 10), random.randint(1, 10))

    nx.set_edge_attributes(G, name='tu', values={e: t[0] for e, t in thresholds.items()})
    nx.set_edge_attributes(G, name='tv', values={e: t[1] for e, t in thresholds.items()})

    return EdgeThresholdsGraphWithTerminals(G, terminals, thresholds)
