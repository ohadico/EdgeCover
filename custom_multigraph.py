import networkx as nx

from graph_factory.graph_converter import convert_to_multigraph

G = nx.MultiGraph()

terminals = '12'
nodes = '3'

G.add_edge('1', '3', tu=5, tv=20)
G.add_edge('1', '3', tu=10, tv=10)
G.add_edge('2', '3', tu=5, tv=20)
G.add_edge('2', '3', tu=10, tv=10)
G.add_edge('2', '3', tu=20, tv=5)

multigraph = convert_to_multigraph(G, terminals)
multigraph.set_bipartite(False)
multigraph.draw(rotate=False, save='output/custom_multigraph.png')
