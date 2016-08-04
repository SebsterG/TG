import numpy as np
import matplotlib.pyplot as plt






E_k = np.loadtxt(open("E_k_32.txt"))
#E_k_oasis = np.loadtxt(open("dkdt.txt"))
E_k_oasis = np.loadtxt(open("Ek_oasis_garra.txt"))

dt = 20.0/len(E_k)
#dt_oasis = 10.0/len(E_k_oasis)

dkdt = -(E_k[1:]-E_k[:-1])/dt
dkdt_oasis = -(E_k_oasis[1:]-E_k_oasis[:-1])/0.001
"""
dkdt_oasis = np.loadtxt(open("results/IPCS/dkdt_oasis.txt"))

dkdt = np.loadtxt(open("results/IPCS/dKdt.txt"))
e_k = np.loadtxt(open("results/IPCS/e_k.txt")) """

print len(dkdt)
time = np.linspace(0,20,200)
time2 = np.linspace(0,20,199)

#time1 = len(dkdt_oasis)
#time2 = 20.0/len(dkdt)



#dkdt = np.loadtxt(open("data_dkdt_2.txt"))
#time = np.loadtxt(open("data_time_2.txt"))
#plt.plot(E_k, label = "kinetic energy")
plt.figure(1)
#plt.plot(time,dkdt,"r", label = "IPCS")
plt.plot(time2,dkdt,"b",label="Chorin")
print len(dkdt_oasis), len(time2)
plt.plot(np.linspace(0,10,9999),dkdt_oasis,"r",label="Oasis")

axes = plt.gca()
legend = axes.legend(loc='upper right', shadow=True)
#plt.figure(2)
#plt.plot(e_k)
plt.show()
