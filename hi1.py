import numpy as np
import matplotlib.pyplot as plt


x=np.array ([100,200,300,400,500,600])
y=np.array([1000,2000,4000,6000,3000,5000])


x1=np.array ([100,200,300,400,500,600])
y1=np.array([100,3000,400,600,300,5000])

plt.scatter(x, y ,c='g',alpha=0.5,edgecolors='black' , marker = "*")


plt.scatter(x1, y1 ,c='b',alpha=0.5,edgecolors='black' , marker = "*")
plt.title("scatter plot")

plt.tight_layout()
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt


x=np.array ([100,200,300,400,500,600])

plt.hist(x,bins=10)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()