import functools
squar = lambda no1,no2: no1+no2

print("enter the numbers:")

value = list(map(int,input().split()))

sun = functools.reduce(squar,value)

print("it is total numbers  :",sun)
