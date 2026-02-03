# 1.Create numpy array of size (2, 3) filled with zeros
import numpy as np
np.zeros((2, 3))

# 2.Create a integer numpy array of (5, 10) filled with ones
np.ones((5, 10), dtype=int)

# 3.Combine two numpy array (3, 2) + (2, 2) => (5, 2)
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[7, 8], [9, 10]])
np.vstack((a, b))

# 4.Convert 2d to 1d
c = np.array([[1, 2, 3], [4, 5, 6]])
c.flatten()

# 5.Interchange two axis of an array
d = np.array([[1, 2, 3], [4, 5, 6]])
d.T

# 6. Create a (2, 3, 5) numpy array with random integer values
np.random.randint(0, 100, size=(2, 3, 5))

# Slice a 3D array
a = np.array([
    [
        [2, 3, 4],
        [5, 6, 7],
        [5, -2, -3]
    ],
    [
        [2, 6, 72],
        [5, -6, 7],
        [3, 5, 4]
    ]
])

# a.
a[:, 1:, 1:]

# b.
a[0, 0:2, 1:]

# c.
a[1, 1:, 1:]

# d.
a[1, 1:2, 1:]

# e.
a[:, :2, 1:]