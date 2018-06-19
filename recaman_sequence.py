import matplotlib
from matplotlib import patches as pat
from matplotlib import pyplot as plt
import numpy as np

nmax = 60

seq = [0]

for i in range(1, nmax):
    if (seq[-1] - i in seq) or (seq[-1] - i < 0):
        seq.append(seq[-1] + i)
    else:
        seq.append(seq[-1] - i)

fig = plt.figure()
ax = fig.add_subplot(111)
for i in range(len(seq) - 1):
    e1 = pat.Arc((0.5*(seq[i] + seq[i+1]), 0), abs(seq[i+1] - seq[i]), abs(seq[i+1] - seq[i]), (((-1)**i+1)*0.5)*180, 180, linewidth = 1, fill = False)

    ax.add_patch(e1)

ax.set_xlim(0, max(seq))
ax.set_ylim(-0.5*max(seq), 0.5*max(seq))
ax.set_aspect('equal')
plt.text(0, -45, 'Coded by J. Saffer', fontsize = 8)
plt.scatter(seq, -40*np.ones_like(seq), marker = 'D', c = np.linspace(0, nmax, nmax), cmap = 'viridis')
plt.savefig('recaman.pdf')
plt.show()
