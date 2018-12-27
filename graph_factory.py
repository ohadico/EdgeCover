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

    return EdgeThresholdsGraphWithTerminals(G, terminals, thresholds)


def create_edge_thresholds_graph_with_terminals_bipartite():
    G = nx.Graph()

    nodes = map(str, range(1, 3))
    terminals = map(str, range(3, 8))

    n1 = nodes[0]
    for n2 in "567":
        G.add_edge(n1, n2, tu=random.randint(1, 10), tv=random.randint(1, 10))

    n1 = nodes[1]
    for n2 in "34":
        G.add_edge(n1, n2, tu=random.randint(1, 10), tv=random.randint(1, 10))

    return EdgeThresholdsGraphWithTerminals(G, terminals, None, is_bipartite=True)

