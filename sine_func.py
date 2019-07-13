import numpy as np
import time

t_amostragem = int(conflista[i+1])/0.1
V_inic = int(instrument.read_register(1,0))
amp = int(conflista[i+2])/2
instrument.write_register(100, 1)
instrument.write_register(101, 1)
for i in range (1, t_amostragem):
    V_ripple = V_inic + amp*np.sen((np.pi*i/10)+(3*np.pi/2)) + amp
    instrument.write_register(683, V_ripple)
    print (seno)
    time.sleep(0.1)

