import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

ax = plt.axes(projection='3d')
# ax.scatter(3, 5, 7)
# plt.show()

x_data = np.random.randint(1, 100, (500,))
y_data = np.random.randint(1, 100, (500,))
z_data = np.random.randint(1, 100, (500,))

ax.scatter(x_data, y_data, z_data, marker="v", alpha=0.5)

plt.show()