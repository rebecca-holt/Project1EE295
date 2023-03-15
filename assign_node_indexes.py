# from classes.Resistors import assign_indices_in_resistors
# from classes.Nodes import assign_node_indexes
# from classes.VoltageSources import assign_node_indexes_in_vs
# from classes.Inductors import assign_indices_in_inductors

from classes.Resistors import Resistors
from classes.Nodes import Nodes
from classes.VoltageSources import VoltageSources
from classes.Inductors import Inductors

def assign_node_indexes(devices):
    node_dict = {}

    nodes = devices["nodes"]

    # Each node is assigned an index
    node_index_counter = 0
    for node in nodes:
        if node.name != "gnd":
            node_index_counter = node.assign_index_in_nodes(node_index_counter, node_dict)
    print("node_index_counter after Nodes: ", node_index_counter)
    
    for node in nodes:
        if node.name != "gnd":
            print("Node name is %s and node index is %g" % (node.name, node.idx))
            print("Node name is %s and node index is %g" % (node.name, node_dict[node.name]))

    # Resistor needs the index
    for resistor in devices["resistors"]:
        resistor.assign_indices_in_resistors(node_dict)

        if resistor.from_node != "gnd":
            print("Resistor from node name is %s and from node index is %g" % (resistor.from_node, resistor.r))
            
        # if resistor.to_node != "gnd":
        #     print("Resistor to node name is %s and to node index is %g" % (resistor.to_node, resistor.to_node_idx))
    # Voltage sources
    for vs in devices["voltage_sources"]:
        node_index_counter = vs.assign_node_indexes_in_vs(node_index_counter, node_dict)
        print("VS from node name is %s" % (vs.amp_ph_ph_rms))
        
    print("node_index_counter after VS: ", node_index_counter)   

    # # Inductor needs the index, but it may also index
    for inductors in devices["inductors"]:
        node_index_counter = inductors.assign_indices_in_inductors(node_index_counter, node_dict)
        print("Inductor from node name is %s and from node index is %g" % (inductors.from_node, inductors.l))
        #adding a volatage source adds two additional nodes
    print("node_index_counter after ind: ", node_index_counter)
    
   
    
    return(node_dict, node_index_counter)
        

        