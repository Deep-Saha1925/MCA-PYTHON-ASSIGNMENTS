import numpy as np
import matplotlib.pyplot as plt

# Create numpy array with values 
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Random 12 integers betwn 20 to 50
y = np.random.randint(20, 50, size=12)

# Create line plt of y vs x
plt.plot(x, y)

# Create numpy array with values
x = np.random.randint(1, 100, size=50)

# Create array by normally distributed values
y = np.random.randn(50)

# PLot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.plot(x, y)

# Create histogram of y with 8 bins
plt.hist(y, bins=8)

# Create boxplot of y
plt.boxplot(y)