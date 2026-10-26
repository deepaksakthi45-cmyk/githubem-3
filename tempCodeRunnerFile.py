
import numpy as np
import matplotlib.pyplot as plt


x=np.array ([100,200,300,400,500,600])

plt.hist(x,bins=10)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()