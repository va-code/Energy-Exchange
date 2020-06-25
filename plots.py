import numpy as np 
import matplotlib.pyplot as plt

x, y = np.loadtxt('base market data.txt', delimiter=',', unpack=True)
print(np.mean(y))
plt.plot(x,y, label='Loaded from file!')
plt.show()
