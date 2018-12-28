import random

from graph_factory.utils import dilute_dict
from graphs.edge_thresholds import EdgeThresholdsGraph
from graphs.edge_thresholds_multigraph import EdgeThresholdsMultiGraph
from graphs.facility_location import FacilityLocation


def generate_graph(t, nt, num_of_edges=None):
    """
    Generate and return a random EdgeThresholdsGraph
    :param t: number of terminals
    :param nt: number of non terminals
    :param num_of_edges: None means full graph, negative means num of edges to throw from full graph
    :return: EdgeThresholdsGraph
    """
    nodes = map(str, range(1, 1 + t + nt))
    terminals = nodes[nt:]
    thresholds = {}

    for i, n1 in enumerate(nodes[:-1]):
        for n2 in nodes[i + 1:]:
            if n1 != n2:
                thresholds[(n1, n2)] = (random.randint(1, 10), random.randint(1, 10))

    thresholds = dilute_dict(thresholds, num_of_edges)

    return EdgeThresholdsGraph(terminals, thresholds)


def generate_multigraph(t, nt, n=1, num_of_edges=None):
    """
    Generate and return a random EdgeThresholdsMultiGraph
    :param t: number of terminals
    :param nt: number of non terminals
    :param n: number of edges between 2 nodes
    :param num_of_edges: None means full n-multigraph, negative means num of edges to throw from full graph
    :return: EdgeThresholdsMultiGraph
    """
    nodes = map(str, range(1, 1 + t + nt))
    terminals = nodes[nt:]
    thresholds = {}

    for i, n1 in enumerate(nodes[:-1]):
        for n2 in nodes[i + 1:]:
            if n1 != n2:
                for e in range(n):
                    thresholds[(n1, n2, e)] = (random.randint(1, 10), random.randint(1, 10))

    thresholds = dilute_dict(thresholds, num_of_edges)

    return EdgeThresholdsMultiGraph(terminals, thresholds)


def generate_bipartite_graph(t, nt, num_of_edges=None):
    """
    Generate and return a random bipartite EdgeThresholdsGraph
    :param t: number of terminals
    :param nt: number of non terminals
    :param num_of_edges: None means full bipartite graph, negative means num of edges to throw from full graph
    :return: EdgeThresholdsGraph
    """
    nodes = map(str, range(1, 1 + t + nt))
    terminals = nodes[nt:]
    thresholds = {}

    for n in nodes[:nt]:
        for t in terminals:
            thresholds[(n, t)] = (random.randint(1, 10), random.randint(1, 10))

    thresholds = dilute_dict(thresholds, num_of_edges)

    return EdgeThresholdsGraph(terminals, thresholds)


def generate_stars_graph(s, l):
    """
    Generate and return a random Forest of Stars
    :param s: number of stars
    :param l: number of leafs
    :return: EdgeThresholdsGraph
    """
    nodes = map(str, range(1, 1 + s + l))
    terminals = nodes[l:]
    division = [0] + sorted([int(random.random() * s)] * (l - 1)) + [s]
    thresholds = {}

    for i, n in enumerate(nodes[:l]):
        for s in terminals[division[i]:division[i + 1]]:
            thresholds[(n, s)] = (random.randint(1, 10), random.randint(1, 10))

    return EdgeThresholdsGraph(terminals, thresholds)


def generate_facility_location_graph(f, c, opening_costs_range, service_costs_range, num_of_edges=None):
    """
    Generate and return a random EdgeThresholdsGraph that represent an instance of Facility Location problem
    :param f: num_of_facilities
    :param c: num_of_clients
    :param opening_costs_range: int tuple of (lo, hi) lo included, hi excluded
    :param service_costs_range: int tuple of (lo, hi) lo included, hi excluded
    :param num_of_edges: None means full graph, negative means num of edges to throw from full graph
    :return:
    """
    nodes = map(str, range(1, 1 + f + c))
    facilities = nodes[:f]
    clients = nodes[f:]

    opening_costs = {f: random.randrange(*opening_costs_range) for f in facilities}
    service_costs = {(c, f): random.randrange(*service_costs_range) for c in clients for f in facilities}

    service_costs = dilute_dict(service_costs, num_of_edges)

    return FacilityLocation(opening_costs, service_costs)


def generate_bipartite_multigraph(t, nt, e=1, num_of_edges=None):
    """
    Generate and return a random bipartite EdgeThresholdsMultiGraph
    :param t: number of terminals
    :param nt: number of non terminals
    :param e: number of edges between 2 nodes
    :param num_of_edges: None means full n-multigraph, negative means num of edges to throw from full graph
    :return: EdgeThresholdsMultiGraph
    """
    nodes = map(str, range(1, 1 + t + nt))
    terminals = nodes[nt:]
    thresholds = {}

    for n in nodes[:nt]:
        for t in terminals:
            if n != t:
                for i in range(e):
                    thresholds[(n, t, i)] = (random.randint(1, 10), random.randint(1, 10))

    thresholds = dilute_dict(thresholds, num_of_edges)

    return EdgeThresholdsMultiGraph(terminals, thresholds)
