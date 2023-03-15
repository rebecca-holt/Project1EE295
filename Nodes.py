import sys
sys.path.append("..")
import numpy as np
from itertools import count

class Nodes:    
    idx=0
    def __init__(self, name, phase):
        self.name = name
        self.phase = phase
        
        # You are welcome to / may be required to add additional class variables   

    # Some suggested functions to implement, 
    def assign_index_in_nodes(self, node_index_counter, node_dict):
        self.idx = node_index_counter
        node_dict[self.name] = node_index_counter
        node_index_counter+=1
        return(node_index_counter)
        
    