import numpy as np
import matplotlib.pyplot as plt
data01_axis1, data01_value1 = np.loadtxt("./true01.txt", unpack=True)


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.plot(data01_axis1, data01_value1, "o-", color="k", label="data01")
ax.set_xlim(-7.0, 15.0)
ax.set_ylim(-7.0, 15.0)
ax.set_xlabel("x label")
ax.set_ylabel("y label")
ax.legend(loc="upper left")
plt.show()