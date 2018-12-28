import random

from graphs.edge_thresholds import EdgeThresholdsGraph
from graphs.edge_thresholds_multigraph import EdgeThresholdsMultiGraph


def create_full_graph(t, nt):
    nodes = map(str, range(1, 1 + t + nt))
    terminals = nodes[nt:]
    thresholds = {}

    for i, n1 in enumerate(nodes[:-1]):
        for n2 in nodes[i + 1:]:
            if n1 != n2:
                thresholds[(n1, n2)] = (random.randint(1, 10), random.randint(1, 10))

    return EdgeThresholdsGraph(terminals, thresholds)


def create_full_multigraph(t, nt, n=1):
    nodes = map(str, range(1, 1 + t + nt))
    terminals = nodes[nt:]
    thresholds = {}

    for i, n1 in enumerate(nodes[:-1]):
        for n2 in nodes[i + 1:]:
            if n1 != n2:
                for e in range(n):
                    thresholds[(n1, n2, e)] = (random.randint(1, 10), random.randint(1, 10))

    return EdgeThresholdsMultiGraph(terminals, thresholds)


def create_bipartite_graph(t, nt):
    nodes = map(str, range(1, 1 + t + nt))
    terminals = nodes[nt:]
    thresholds = {}

    for n in nodes[:nt]:
        for t in terminals:
            thresholds[(n, t)] = (random.randint(1, 10), random.randint(1, 10))

    return EdgeThresholdsGraph(terminals, thresholds)


def create_stars_graph(t, nt):
    nodes = map(str, range(1, 1 + t + nt))
    terminals = nodes[nt:]
    division = [0] + sorted([int(random.random() * t)] * (nt - 1)) + [t]
    thresholds = {}

    for i, n in enumerate(nodes[:nt]):
        for t in terminals[division[i]:division[i+1]]:
            thresholds[(n, t)] = (random.randint(1, 10), random.randint(1, 10))

    return EdgeThresholdsGraph(terminals, thresholds)
