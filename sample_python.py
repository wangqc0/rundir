# This is a sample file.

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x, y = np.random.normal(loc = 100, scale = 15, size = (2, 100))

plt.scatter(x, y)
plt.savefig('sample_python_graph.png')
