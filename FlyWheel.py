from math import pi
from scipy.constants import g
import numpy as np
N = [18.01,14.1499,14.3615,10.8413]
n =[5,5,4,4]
m =[0.3,0.25,0.3,0.25]
h = [0.33,0.33,0.257,0.257]
t = [22.81,18.98,18.85,17.87]
r = 1.99*10**-2
obv= 4
Iarray = []
Isum = 0
for i in range(obv):
    I = N[i]*m[i]/(N[i]+n[i])*((2*g*h[i]/(4*pi*N[i]/t[i])**2)-r**2)
    Iarray.append(I)
    Isum += I

Iavg = Isum/obv
Deviation = []
Dsum = 0
for i in range(obv):
    D = np.abs(Iavg-Iarray[i])
    Deviation.append(D)
    Dsum += D**2
error= Dsum**(1/2)/(obv**(1/2)*(obv-1)**(1/2))
print(f"{Iavg} \u00B1 {error}")

