import networkx as nx

from graph_factory.utils import new_node_name
from graphs.edge_thresholds import EdgeThresholdsGraph
from graphs.edge_thresholds_multigraph import EdgeThresholdsMultiGraph
from graphs.facility_location import FacilityLocation


def convert_to_graph(G, terminals, t1='tu', t2='tv'):
    """

    :param G:
    :type G: nx.Graph
    :param terminals:
    :param t1:
    :param t2:
    :return:
    """
    thresholds = {e: (d[t1], d[t2]) for e, d in G.edges.items()}
    return EdgeThresholdsGraph(terminals, thresholds)


def convert_to_multigraph(G, terminals, t1='tu', t2='tv'):
    """

    :param G:
    :type G: nx.MultiGraph
    :param terminals:
    :param t1:
    :param t2:
    :return:
    """
    thresholds = {e: (d[t1], d[t2]) for e, d in G.edges.items()}
    return EdgeThresholdsMultiGraph(terminals, thresholds)


def convert_to_facility_location(G, k='weight'):
    """

    :param G:
    :type G: nx.Graph
    :param k:
    :return:
    """
    facilities = {n for n in G.nodes if k in G.nodes[n] and G.nodes[n][k] != 0}
    opening_costs = {f: G.nodes[f][k] for f in facilities}
    service_costs = {}
    for e, d in G.edges.items():
        if e[0] in facilities:
            e = e[::-1]
        service_costs[e] = d[k]

    return FacilityLocation(opening_costs, service_costs)


def reduce_levels(graph, levels=None):
    """

    :param graph:
    :type graph: EdgeThresholdsMultiGraph
    :return:
    """
    nodes = graph.get_nonterminals()
    if levels is None:
        levels = {t[0] for e, t in graph.get_thresholds()}
    nodes_levels = {new_node_name(n, l): l for n in nodes for l in levels}

    thresholds = {}
    for e, t in graph.get_thresholds():
        n1, n2, i = e
        level, cost = t
        thresholds[(n2, new_node_name(n1, level))] = cost

    return FacilityLocation(nodes_levels, thresholds)
