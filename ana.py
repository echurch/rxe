### source ~/pfis/venv/bin/activate

from ROOT import TFile
from root_numpy import root2array, tree2array
import numpy as np

f = TFile("ACTAA.e-s.400keV_10atm.root") # ACTAA.gammas.40keV_10atm.root
array = tree2array(f.ACTAATree)

q = np.zeros(f.ACTAATree.GetEntries())

for i in range(f.ACTAATree.GetEntries()):
    q[i] = array[i]["sdq"].sum()


import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

plt.plot(array[0]["sdx"],array[0]["sdy"])
plt.axis([-65,+65,-65,+65]) # 13 cm (130 mm) radius
plt.title('x-y trajectories')
plt.plot(array[1]["sdx"],array[1]["sdy"])
plt.plot(array[2]["sdx"],array[2]["sdy"])
plt.plot(array[3]["sdx"],array[3]["sdy"])
plt.plot(array[4]["sdx"],array[4]["sdy"])
plt.savefig("xy-e400keV10atm-trajectories.pdf")
plt.close()

n, bins, patches = plt.hist(q, 50)
plt.title('energysum')
plt.savefig("energysum-e400keV10atm-trajectory.pdf")
