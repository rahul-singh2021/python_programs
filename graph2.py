import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints,'#444444',marker='.')

y1points = np.array([0, 200])

plt.plot(xpoints,y1points,'b--')

plt.legend(['all','not all'])
plt.show()
