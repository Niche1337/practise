import random

a = random.sample(range(0,100),10)
b = []
x = []
print(a)

for i in a:
    if i < 50:
        b.append(i)
print(b)

c = int(input("Tell us a number "))

for i in a:
    if i < c:
        x.append(i)
print(x)





