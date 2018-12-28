import networkx as nx

from graph_factory.graph_converter import convert_to_graph

G = nx.Graph()
terminals = ['1', '2']
nodes = ['3', '4', '5']

G.add_edge('1', '5', tu=5, tv=20)
G.add_edge('1', '4', tu=10, tv=10)
G.add_edge('2', '5', tu=5, tv=20)
G.add_edge('2', '4', tu=10, tv=10)
G.add_edge('2', '3', tu=20, tv=5)

graph = convert_to_graph(G, terminals)
graph.draw(rotate=False, save='output/custom_graph.png')
