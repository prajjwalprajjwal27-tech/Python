squar = lambda no: no%2

print("enter the numbers:")

value = list(map(int,input().split()))

sun = list(filter(squar,value))

print("it is odd numbers  :",sun)
