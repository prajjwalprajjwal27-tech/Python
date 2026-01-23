import functools
squar = lambda no1,no2:no1 if no1 <no2 else no2

print("enter the numbers:")

value = list(map(int,input().split()))

sun = functools.reduce(squar,value)

print("it is maniumam  numbers  :",sun)
