from graph_factory.edge_thresholds import create_facility_location

graph = create_facility_location(3, 5, (1, 2), (0, 1), -7)
graph.draw(tu=0.03, save="output/set_cover.png")
