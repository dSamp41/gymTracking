import numpy as np
import matplotlib.pyplot as plt


fig1, ax1 = plt.subplots()
ax1.set_title('Example')

d1 = np.array([23,24,25,28])
d2 = np.array([24,25,28,30])

m1, m2 = np.mean(d1), np.mean(d2)

ax1.boxplot([d1, d2])
ax1.plot([1,2], [m1,m2])


plt.show()