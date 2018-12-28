import operator
import matplotlib.pyplot as plt

from graphs.edge_thresholds import EdgeThresholdsGraph


class FacilityLocation(EdgeThresholdsGraph):
    def __init__(self, opening_costs, service_costs, **attr):
        terminals = set(map(operator.itemgetter(0), service_costs.keys()))
        thresholds = {e: (c, opening_costs[e[1]]) for e, c in service_costs.items()}
        super(FacilityLocation, self).__init__(terminals, thresholds, **attr)

    def _draw_thresholds(self, pos, tu, tv):
        facilities = self.get_nonterminals()
        opening_costs = self.get_opening_costs(facilities)
        for f in facilities:
            plt.text(pos[f][0] + tu, pos[f][1] + tu,
                     opening_costs[f])

        edge_labels = {e: t[0] for e, t in self.get_thresholds()}
        self._draw_edge_labels(pos, edge_labels, tv)

    def get_opening_costs(self, facilities):
        opening_costs = {}
        for e in self.get_edges_sorted():
            c, f = e
            s, o = self.get_thresholds_at(e)
            opening_costs[f] = o
            if len(opening_costs) == len(facilities):
                break
        return opening_costs
