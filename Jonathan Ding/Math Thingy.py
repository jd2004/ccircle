from math import*
print("Enter a number, is it a prime?")
n=int(input())
m=ceil(sqrt(n))
o=range(2,m)
IsPrime=True
for i in o:
    if n == 0%i:
        IsPrime=False
if n<=1:
    print("IT'S NOT PRIME OR COMPOSITE")
elif IsPrime==True:
    print("IT'S PRIME")
elif IsPrime==False:
    print("IT'S COMPOSITE")
print("Enter a number, n. What is the nth Fibonacci number?")
x=int(input())
y=range(1,x)
for i in y:
    1+1