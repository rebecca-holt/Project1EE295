import numpy as np

def initialize(devices, size_Y):
    V_init = np.zeros((size_Y,), dtype=float)
    print("V_init: ", V_init)
    return V_init