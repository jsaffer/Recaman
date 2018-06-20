import matplotlib
from matplotlib import patches as pat
from matplotlib import pyplot as plt
import numpy as np

nmax = 66

seq = [0]

for i in range(1, nmax):
    if (seq[-1] - i in seq) or (seq[-1] - i < 0):
        seq.append(seq[-1] + i)
    else:
        seq.append(seq[-1] - i)

fig = plt.figure()
ax = fig.add_subplot(111)
for i in range(len(seq) - 1):
    e1 = pat.Arc((0.5*(seq[i] + seq[i+1]), 0), abs(seq[i+1] - seq[i]), abs(seq[i+1] - seq[i]), (((-1)**(i+1)+1)*0.5)*180, 180, linewidth = 1, fill = False)

    ax.add_patch(e1)

edge_factor = 1.05
ax.set_xlim(-(edge_factor-1)*max(seq), edge_factor*max(seq))
ax.set_ylim(-0.5*edge_factor*nmax, 0.5*edge_factor*nmax)
ax.set_aspect('equal')
#plt.scatter(seq, -0.5*(edge_factor*nmax)*np.ones_like(seq)+1, marker = 'D', c = np.linspace(0, nmax, nmax), cmap = 'viridis')
plt.savefig('recaman.pdf')
plt.show()
