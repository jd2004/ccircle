'''from math import*
print("Enter a number, is it a prime?")
n=int(input())
m=ceil(sqrt(n))
o=range(2, m)
IsPrime=True
for i in o:
    if n == 0 % i:
        IsPrime = False
if n<=1:
    print("IT'S NOT PRIME OR COMPOSITE")
elif IsPrime == True:
    print("IT'S PRIME")
elif IsPrime == False:
    print("IT'S COMPOSITE")'''
from math import *

def numbers_squared_dict(a):
    d = {}
    for i in range(1, a+1):
        d[i] = i**2
    return d

#print(numbers_squared_dict(10))

import operator

d = {
    1: 4,
    4: 3,
    7: 5,
    2: 9,
    3: 1
}

def sort_by_key(dict):
    return sorted(dict)

#print(sort_by_key(d.items()))


def dst(a, b, c, d):
    return sqrt((a - b)**2 + (c - d)**2)

print(dst(0, 3, 0, 4))
