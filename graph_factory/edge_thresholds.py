import random

import networkx as nx

from graphs.edge_thresholds import EdgeThresholdsGraph

random.seed(6)


def create_full_graph(t, nt):
    nodes = map(str, range(1, 1 + t + nt))
    terminals = nodes[nt:]
    thresholds = {}

    for i, n1 in enumerate(nodes[:-1]):
        for n2 in nodes[i + 1:]:
            if n1 != n2:
                thresholds[(n1, n2)] = (random.randint(1, 10), random.randint(1, 10))

    return EdgeThresholdsGraph(terminals, thresholds)


def create_bipartite_graph(t, nt):
    nodes = map(str, range(1, 1 + t + nt))
    terminals = nodes[nt:]
    division = [0] + sorted([int(random.random() * t)] * (nt - 1)) + [t]
    thresholds = {}

    for i, n in enumerate(nodes[:nt]):
        for t in terminals[division[i]:division[i+1]]:
            thresholds[(n, t)] = (random.randint(1, 10), random.randint(1, 10))

    return EdgeThresholdsGraph(terminals, thresholds)
