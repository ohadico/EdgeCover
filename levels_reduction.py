from graph_factory.graph_generator import generate_facility_location_graph

graph = generate_facility_location_graph(2, 3, (5, 20), (5, 20), -1)

graph.draw(tu=-0.025, tv=0.8, rotate=False,
           save="output/levels_reduction.png")
