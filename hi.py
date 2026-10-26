from pandas import merge
from sympy import li


m = "Hello, World!"
print(type(m))

number = [1,2,3,4,5]
number.insert(1,6)
number.pop(0)
print(number)

count=0
number = [1,2,3,4,5]
print(number[0])
print(type(number))
print(len(number))
count+=1
print(count)    

a=[10,20,30,10,40,7]
b=a.copy()                            
b.append(10)
print(a)
print(b)
print(a==b)
print(20 in b)
print(a[::-1])
a.pop(1)
print(a)
print(a.index(30))
print(sorted(a))
print(a.count(10))
number=a
number=list(dict.fromkeys(number))
print(number)

number = list(filter(lambda x: x%2==0, number))
print(number)
a = list(map(lambda n:n*n, number))
print(a)


a=[10,20,30,10,40,7]
b=[10,20,30,10,40,7]

number= list(zip(a,b))
print(number)
number=list(enumerate(b, start=1))
print(number)

number={1,2,3,4,5,6,7}
tamil=(list(number))
print(tamil)

import random 
otp=random.choice(range(10000,100000))
print(otp)



number = [1,2,3,4,5]
langrest_number=number[0]
for i in number:
    if i>langrest_number:
        langrest_number=i   
print(langrest_number)





import matplotlib.pyplot as plt
import numpy as np

figure, axes = plt.subplots(2, 2)

x = np.array(
    [2021,2022,2023,2024,2025,2026]
    )

y=np.array(
    [1000,2000,3000,4000,5000,6000]
    )

axes[0, 0].plot(x,y)
plt.show()


import matplotlib.pyplot as plt
import numpy as np

figure, axes = plt.subplots(2, 2)

x = np.array([2022, 2024, 2025, 2029, 2030, 2031])
y = np.array([1000, 1300, 4000, 5000, 1000, 6000])
x1 = np.array([2022, 2024, 2025, 2029, 2030, 2031])
y1 = np.array([1000, 1300, 4000, 5000, 1000, 6000])
axes[0, 1].bar(x, y,c='r')
axes[0, 0].scatter(x1, y1,c='g')
plt.show()



import matplotlib.pyplot as plt
import numpy as np

figure,axes=plt.subplots(2,2)

x=np.array([2022,2024,2025,2029,2030,2031])
y=np.array([1000,1300,4000,5000,1000,6000])

axes[1,0].plot(x,y)
plt.show()





import matplotlib.pyplot as plt
import numpy as np

figure, axes = plt.subplots(2, 2)

x = np.array([2022, 2024, 2025, 2029, 2030, 2031])
y = np.array([1000, 1300, 4000, 5000, 1000, 6000])

axes[0, 1].bar(x, y, color='r')
axes[0, 0].scatter(x, y, color='g')
plt.tight_layout()
plt.show()

import pandas as pd

df=pd.read_csv('data.csv')
import matplotlib.pyplot as plt
import numpy as np

figure, axes = plt.subplots(2, 2)

x = np.array([2022, 2024, 2025, 2029, 2030, 2031])
y = np.array([1000, 1300, 4000, 5000, 1000, 6000])

axes[0, 1].bar(x, y, color='r')
axes[0, 0].scatter(x, y, color='g')

plt.tight_layout()
plt.show()

import pandas as pd

df=pd.read_csv(import matplotlib.pyplot as plt
import numpy as np

figure, axes = plt.subplots(2, 2)

x = np.array([2022, 2024, 2025, 2029, 2030, 2031])
y = np.array([1000, 1300, 4000, 5000, 1000, 6000])

axes[0, 1].bar(x, y, color='r')
axes[0, 0].scatter(x, y, color='g')

plt.tight_layout()
plt.show()

import pandas as pd

df=pd.read_csv(r"C:\Users\deepa\Downloads\customers-100.csv")
print(df["City"].to_string())
      


number=[1,2,3,4,5,5,6,7,8]
print(list(dict.fromkeys(number)))


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\deepa\Downloads\customers-100.csv")
print(df)
