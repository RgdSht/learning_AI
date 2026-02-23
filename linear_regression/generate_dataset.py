import numpy as np

np.random.seed(42)

size = np.random.rand(1000, 1) * 200  # size in m2
rooms = np.random.randint(1, 6, (1000, 1))

price = 3000 * size + 10000 * rooms + 50000
price += np.random.randn(1000, 1) * 10000  # noise