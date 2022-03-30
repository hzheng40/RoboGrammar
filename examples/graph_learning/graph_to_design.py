import numpy as np
import quaternion
import pyrobotdesign as rd
from design_search import make_initial_graph, build_normalized_robot, get_applicable_matches, has_nonterminals

class GraphBuilder:
    def __init__(self, grammar_file):
        self.graphs = rd.load_graphs(grammar_file)

    def build_robot_from_adj(self, adj):
        initial_graph = make_initial_graph()
        # TODO: