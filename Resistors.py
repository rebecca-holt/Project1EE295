
import numpy as np
from itertools import count
from classes.Nodes import Nodes
# from lib.stamping_functions import stamp_y_sparse, stamp_j_sparse


class Resistors:
    def __init__(self, name, from_node, to_node, r):
        self.name = name
        self.from_node = from_node
        self.to_node = to_node
        self.r = r
        # You are welcome to / may be required to add additional class variables   

    # Some suggested functions to implement, 
    def assign_indices_in_resistors(self, node_dict):
        if self.from_node != "gnd":
            self.from_node_idx = node_dict[self.from_node]
        if self.to_node != "gnd":
            self.to_node_idx = node_dict[self.to_node]
        
    def stamp_sparse(self,):
        pass

    def stamp_dense_R(self, Y, node_index_dict):
        if self.from_node != "gnd":
            i = node_index_dict[self.from_node]
            Y[i, i] += 1/self.r
        if self.to_node != "gnd":
            j = node_index_dict[self.to_node]
            Y[j, j] += 1/self.r
        if self.from_node != "gnd" and self.to_node != "gnd":
            Y[i, j] += -1/self.r
            Y[j, i] += -1/self.r
        