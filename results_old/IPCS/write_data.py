import numpy as np
import matplotlib.pyplot as plt





dkdt = np.loadtxt(open("dkdt_32.txt"))
E_k_oasis = np.loadtxt(open("Ek_oasis_garra.txt"))
dkdt_oasis = -(E_k_oasis[1:]-E_k_oasis[:-1])/0.001


print len(dkdt)
time = np.linspace(0,20,200)
time2 = np.linspace(0,20,199)

plt.figure(1)
plt.plot(time,dkdt,"b",label="IPCS")
print len(dkdt_oasis), len(time2)
plt.plot(np.linspace(0,10,9999),dkdt_oasis,"r",label="Oasis")

axes = plt.gca()
legend = axes.legend(loc='upper right', shadow=True)
#plt.figure(2)
#plt.plot(e_k)
plt.show()
