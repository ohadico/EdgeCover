import networkx as nx

from graph_factory.graph_converter import convert_to_facility_location

G = nx.Graph()

facilities = 'ABC'
facilities_weights = (35, 85, 43)
clients = map(str, range(1, 6))

for f, w in zip(facilities, facilities_weights):
    G.add_node(f, weight=w)

G.add_edges_from(('1A', '3A', '3C'), weight=1)
G.add_edges_from(('1B', '2A', '4C', '5C'), weight=2)
G.add_edges_from(('2B', '4B', '5B'), weight=3)
G.add_edges_from(('2C', '4A'), weight=4)
G.add_edges_from(('3B',), weight=5)


graph = convert_to_facility_location(G)
graph.draw(tu=0.15, tv=0.03, rotate=False,
           save='output/custom_facility_location.png')
