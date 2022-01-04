import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-10,10,100)

# Below is the actual function:
y = x**2

# this then plots the function
plt.plot(x,y, 'b')

# this command then actually shows the plot
plt.show()