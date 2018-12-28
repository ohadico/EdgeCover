import random

from graphs.edge_thresholds import EdgeThresholdsGraph
from graphs.edge_thresholds_multigraph import EdgeThresholdsMultiGraph
from graphs.facility_location import FacilityLocation


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


def create_bipartite_graph(t, nt, num_of_edges=None):
    """

    :param t:
    :param nt:
    :param num_of_edges: None means full bipartite, negative number is substracted from the full bipartite graph
    :return:
    """
    nodes = map(str, range(1, 1 + t + nt))
    terminals = nodes[nt:]
    thresholds = {}

    for n in nodes[:nt]:
        for t in terminals:
            thresholds[(n, t)] = (random.randint(1, 10), random.randint(1, 10))

    if num_of_edges is not None:
        if num_of_edges < 0:
            num_of_edges = len(thresholds) + num_of_edges
        edges = random.sample(thresholds, num_of_edges)
        thresholds = {e: t for e, t in thresholds.items() if e in edges}

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


def create_facility_location(f, c, opening_costs_range, service_costs_range, num_of_edges=None):
    """

    :param num_of_edges:
    :param f: num_of_facilities
    :param c: num_of_clients
    :param opening_costs_range:
    :param service_costs_range:
    :return:
    """
    nodes = map(str, range(1, 1 + f + c))
    facilities = nodes[:f]
    clients = nodes[f:]

    opening_costs = {f: random.randrange(*opening_costs_range) for f in facilities}
    service_costs = {(c, f): random.randrange(*service_costs_range) for c in clients for f in facilities}

    if num_of_edges is not None:
        if num_of_edges < 0:
            num_of_edges = len(service_costs) + num_of_edges
        edges = random.sample(service_costs, num_of_edges)
        service_costs = {e: t for e, t in service_costs.items() if e in edges}

    return FacilityLocation(opening_costs, service_costs)
