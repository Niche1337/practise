# -*- coding: utf-8 -*-

###---Quicksort---###


x = [11,16,2,8,1,9,4,7]
pivot = x[-1]
wall = 0
current = 0
middle = int( (len(x)/2) - 1)

print(x)
    
for y in x:
    if x[current] < pivot:
        x[wall], x[current] = x[current], x[wall]
        wall = wall + 1
        
    current = current + 1     

x[middle], x[pivot] = x[pivot], x[middle]

subX1 = x[:middle]
subX2 = x[middle+1:]     
print(x)
print(subX1)   
print(subX2)


pivot = subX1[-1]
wall = 0
current = 0
for y in subX1:
    if subX1[current] < pivot:
        subX1[wall], subX1[current] = subX1[current], subX1[wall]
        wall = wall + 1
        
    current = current + 1   



pivot = subX2[-1]
wall = 0
current = 0
for y in subX2:
    if subX2[current] < pivot:
        subX2[wall], subX2[current] = subX2[current], subX2[wall]
        wall = wall + 1
        
    current = current + 1   

print(subX1)   
print(subX2)