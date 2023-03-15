import sys
sys.path.append("..")
import numpy as np
from itertools import count
from classes.Nodes import Nodes
from classes.VoltageSources import VoltageSources
from classes.Resistors import Resistors
# from lib.stamping_functions import stamp_y_sparse, stamp_j_sparse

class Inductors:
    def __init__(self, name, from_node, to_node, l):
        self.name = name
        self.from_node = from_node
        self.to_node = to_node
        self.l = l  
        

    # Some suggested functions to implement, 
    def assign_indices_in_inductors(self, node_counter,node_dict):
       #if the from node is not equal to ground, assign from node index
       if self.from_node != "gnd":
            self.from_node_idx = node_dict[self.from_node]
        
       #Crease object names for voltage source Vx and negative ref of voltage source, Vn
       self.vx_name = "v_x"
       self.vn_name = "v_n"
       
       #set Vx negative ref voltage index equal to the node counter
       self.comp_vn_node_idx = node_counter 
     
       #Add the node index to the node dictionary
       node_dict[self.name] = self.comp_vn_node_idx
       
       #add on to node counter because extra node, Vn added
       node_counter += 1

       #Add in voltage source------------------------------
       #set the companion voltage source index equal to the new node counter value
       self.comp_vx_node_idx = node_counter
       #Add the node index to the node dictionary
       node_dict[self.vx_name] = self.comp_vx_node_idx
       #Increase the node count by 1 because Vx adds new node
       node_counter += 1
       


 #define companion Vp node index
       #define to node of inductor, if it is not equal to ground
       if self.to_node != "gnd":            
            self.to_node_idx = node_dict[self.to_node]

       #return new node counter value after adding two nodes
       return node_counter

    def stamp_sparse(self,):
        pass

    #stamp in the inductor into the Y and J matrix and vector.
    def stamp_dense(self,Y, J, t,node_index_dict, V,delta_t):
        #Define companion voltage source value
        Vx = 0
        #filling in row of Y matrix with companion voltage source
        Y[self.comp_vx_node_idx, self.from_node_idx] += 1
        Y[self.comp_vx_node_idx, self.comp_vn_node_idx] += -1
        J[self.comp_vx_node_idx] = Vx
        #filling in column of Y matrix with companion voltage source 
        Y[self.from_node_idx, self.comp_vx_node_idx] += 1
        Y[self.comp_vn_node_idx, self.comp_vx_node_idx] += -1
        #define conductance
        g = delta_t/(2*self.l)
        
        Y[self.comp_vn_node_idx, self.comp_vn_node_idx] += g
        if self.to_node != "gnd":
            Y[self.comp_vn_node_idx, self.to_node_idx] += -g
            Y[self.to_node_idx, self.comp_vn_node_idx] += -g
            Y[self.to_node_idx, self.to_node_idx] += g
            
        i_t = V[self.comp_vx_node_idx]
        #vt=V[self.from_node_idx]-V[self.comp_vn_node_idx]
        if self.to_node != "gnd":
            vt=V[self.from_node_idx]-V[self.to_node_idx]
        else: 
            vt=V[self.from_node_idx]
        #Calculate current source
        i_source = i_t + g*(vt)
       
        #stamps in the J vector 
        J[self.comp_vn_node_idx] += -i_source
        #adding dt/2L*V(to_node) to Y matrix and -i_source to J matrix
        if self.to_node != "gnd":
            J[self.to_node_idx] += i_source
      
    def stamp_short(self,):
        pass
    