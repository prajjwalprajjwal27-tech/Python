squar = lambda no: no %2 == 0

print("enter the numbers:")

value = list(map(int,input().split()))

sun = list(filter(squar,value))

print("it is even numbers  :",sun)
