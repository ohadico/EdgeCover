from graph_factory.edge_thresholds import create_bipartite_graph

graph = create_bipartite_graph(5, 2)
nonterminals = graph.get_nonterminals()

graph.draw(node_labels=dict(zip(nonterminals, 'ab')),
           save="output/stars.png")
