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


def create_edge_thresholds_graph_with_terminals_bipartite(t=5, nt=2):
    G = nx.Graph()

    nodes = map(str, range(1, 1 + t + nt))
    terminals = nodes[nt:]
    division = [0] + sorted([int(random.random() * t)] * (nt - 1)) + [t]
    thresholds = {}

    for i, n in enumerate(nodes[:nt]):
        for t in terminals[division[i]:division[i+1]]:
            G.add_edge(n, t)
            thresholds[(n, t)] = (random.randint(1, 10), random.randint(1, 10))

    return EdgeThresholdsGraphWithTerminals(G, terminals, thresholds)
