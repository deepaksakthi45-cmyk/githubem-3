from pandas import merge


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