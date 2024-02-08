import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

ax = plt.axes(projection='3d')

x_data = np.arange(0, 50, 0.1)
y_data = np.arange(0, 50, 0.1)
# z_data = x_data * y_data
# ax.scatter(x_data, y_data, z_data)

z_data = np.sin(x_data) * np.cos(y_data)
ax.plot(x_data, y_data, z_data)

ax.set_title("Funny Func")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")
ax.set_zlabel("Fancy Result")

plt.show()