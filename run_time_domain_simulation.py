import numpy as np
import matplotlib.pyplot as plt
def run_time_domain_simulation(devices, V_init, size_Y, SETTINGS, delta_t,V_a, V_b,V_c,I_a, I_b, I_c):
    t_final = SETTINGS['Simulation Time']
    # for t in range (0, t_final, delta_t)
    #     V_zero[t] = numpy.cos(t)
    t = np.linspace(start=0, stop=t_final, num= len(V_a))
    # plot = plt.figure(1, dpi=1200)
    plt.plot(t, V_a, label="V_a")
    plt.plot(t, V_b, label="V_b")
    plt.plot(t, V_c, label="V_c")
    plt.title("Voltages Va, Vb, and Vc outputs vs time ")
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.legend(loc="upper left")
    #plt.axhline(y=0,linewidth=.5, color='k')
    plt.show()

    plt.plot(t, I_a, label="I_a")
    plt.plot(t, I_b, label="I_b")
    plt.plot(t, I_c, label="I_c")
    plt.title("Currents Ia, Ib, and Ic outputs vs time")
    plt.xlabel('Time (s)')
    plt.ylabel('Current (A)')
    plt.legend(loc="upper left")
    #plt.axhline(y=0,linewidth=.5, color='k')
    plt.show()

    V_waveform = None

    return V_waveform