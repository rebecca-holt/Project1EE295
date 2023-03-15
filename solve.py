
from lib.parse_json import parse_json
from lib.assign_node_indexes import assign_node_indexes
from lib.initialize import initialize
from scripts.run_time_domain_simulation import run_time_domain_simulation
from scripts.process_results import process_results
import numpy as np
from copy import deepcopy

def solve(TESTCASE, SETTINGS):
    """Run the time-domain solver.
    Args:
        TESTCASE (str): A string with the path to the network json file.
        SETTINGS (dict): Contains all the solver settings in a dictionary.
    Returns:
        None
    """
    # TODO: STEP 0 - Initialize all the model classes in the models directory (models/) and familiarize
    #  yourself with the parameters of each model.

    # # # Parse the test case data # # #
    case_name = TESTCASE
    devices = parse_json(case_name)

    # # # Unpack parsed device objects in case you need them # # #
    nodes = devices['nodes']
    voltage_sources = devices['voltage_sources']
    resistors = devices['resistors']
    capacitors = devices['capacitors']
    inductors = devices['inductors']
    switches = devices['switches']
    induction_motors = devices['induction_motors']

    for ele in nodes:
        print(ele.name)

    # # # Solver settings # # #
    t_final = SETTINGS['Simulation Time']
    tol = SETTINGS['Tolerance']  # NR solver tolerance
    max_iters = SETTINGS['Max Iters']  # maximum NR iterations
    delta_t = 10**-5 #time step (s)

    # # # Assign system nodes # # #
    # We assign a node index for every node in our Y matrix and J vector.
    # In addition to voltages, nodes track currents of voltage sources and
    # other state variablesneeded for companion models or the model of the 
    # induction motor.
    # You can determine the size of the Y matrix by looking at the total
    # number of nodes in the system.
    node_index_dict, node_index_counter = assign_node_indexes(devices)
 
    # # # Initialize solution vector # # #
    # TODO: STEP 1 - Complete the function to find your state vector at time t=0.
    #Amrit says add +1 because indexing starts at zero,
    #size_Y = node_index_counter + 1, but this makes matrix one col and row extra zeros
    size_Y = node_index_counter 
    V_init = initialize(devices, size_Y)
    #set t=0 - R
    t=0

    V_prev = V_init
    V_a, V_b, V_b, V_c, I_a, I_b, I_c= ([] for i in range(7))
    
    V = V_init
    while(t <= t_final):
        # Create an empty np.matrix (DENSE) for each time tick
        Y = np.zeros((size_Y, size_Y), dtype=float)
        J = np.zeros((size_Y,), dtype=float)

        # Stamp different things into the matrix
        # Stamp resistors
        for r in resistors:
            r.stamp_dense_R(Y, node_index_dict)

        # Stamp voltages sources
        for vs in voltage_sources:
            vs.stamp_dense_vs(Y, J, t)

        # Stamp inductors
        for i in inductors:
            i.stamp_dense(Y, J, t,node_index_dict, V,delta_t)

        #Solve it
        Vsol = np.linalg.solve(Y, J)

        V = np.copy(Vsol)

        t += delta_t
        
        #add voltage sources to lists to be plotted
        V_a.append(Vsol[6])
        V_b.append(Vsol[7])
        V_c.append(Vsol[8])

        #add current sources to lists to be plotted
        I_a.append(Vsol[22])
        I_b.append(Vsol[24])
        I_c.append(Vsol[26])
       

    print(print("node_dict", node_index_dict))
    print("Vsol: ")
    print(Vsol)
    print("LENGTH VSOL:", len(Vsol))
    # print("Y")
    # print(Y)
    # print("J")
    # print(J)
    # TODO: STEP 2 - Run the time domain simulation and return an array that contains
    #                time domain waveforms of all the state variables # # #
    V_waveform = run_time_domain_simulation(devices, V_init, size_Y, SETTINGS, delta_t,V_a, V_b, V_c,I_a, I_b, I_c)

    # # # Process Results # # #
    # TODO: PART 1, STEP 3 - Write a process results function to compute the relevant results (voltage and current
    # waveforms, steady state values, etc.), plot them, and compare your output to the waveforms produced by Simulink
    process_results(V_waveform, devices)
