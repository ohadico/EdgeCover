from graph_factory.edge_thresholds import create_stars_graph

graph = create_stars_graph(5, 2)
nonterminals = graph.get_nonterminals()

graph.draw(node_labels=dict(zip(nonterminals, 'ab')),
           tv=0.8, save="output/stars.png")
