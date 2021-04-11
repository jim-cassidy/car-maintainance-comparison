import matplotlib.pyplot as plt
import numpy as np


def function(x):
    return ( np.log(x) * 1811 ) - 17135

x = np.arange(0.01,300000,0.1)

y = function(x)

plt.plot(x,y)

plt.grid()

plt.xlim(0,300000)
plt.ylim(0,10000)

plt.title('Average car costs for all cars pery year regression',fontsize=10)

plt.xlabel('x',fontsize=8)
plt.ylabel('log',fontsize=8)

plt.savefig('allcars.png', bbox_inches='tight')
plt.show()
plt.close()
