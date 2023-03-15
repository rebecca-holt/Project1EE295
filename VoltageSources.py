import numpy as np
from itertools import count
from classes.Nodes import Nodes
# from lib.stamping_functions import stamp_y_sparse, stamp_j_sparse
import numpy as np

class VoltageSources:
    def __init__(self, name, vp_node, vn_node, amp_ph_ph_rms, phase_deg, frequency_hz):
        self.name = name
        self.vp_node = vp_node
        self.vn_node = vn_node
        self.amp_ph_ph_rms = amp_ph_ph_rms
        self.amp_ph_ph = amp_ph_ph_rms *np.sqrt(2/3)
        self.phase_deg = phase_deg
        self.frequency_hz = frequency_hz
        self.phase_rad =float(phase_deg)*np.pi/180
        # You are welcome to / may be required to add additional class variables   

    # Some suggested functions to implement, 
    def assign_node_indexes_in_vs(self, node_counter, node_dict):
       #self.vs_idx = node_counter-1
       self.vs_idx = node_counter
       node_dict[self.name] = self.vs_idx
       print("node_dict", node_dict)
       if self.vp_node != "gnd":
        #getting index from node dict
          self.vp_node_idx = node_dict[self.vp_node]
        
       if self.vn_node != "gnd":
          self.vn_node_idx = node_dict[self.vn_node]
      
       node_counter += 1
       return(node_counter)
        
    def stamp_sparse(self,):
        pass

    def stamp_dense_vs(self, Y, J, t):
        #chaning Y and J here changes them everwhere else in the matrix so don't need to return anything
        vt = self.amp_ph_ph * np.cos(2*(np.pi)*self.frequency_hz*t+ self.phase_rad) 
        #filling in row of Y matrix
        Y[self.vs_idx, self.vp_node_idx] += 1
        if self.vn_node != "gnd":
            Y[self.vs_idx, self.vn_node_idx] += -1
        J[self.vs_idx] = vt
        #filling in column of Y matrix
        Y[self.vp_node_idx, self.vs_idx] += 1
        if self.vn_node != "gnd":
            Y[self.vn_node_idx, self.vs_idx] += -1

    def stamp_open(self,):
        pass
    

    
        


    
