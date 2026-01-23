squar = lambda no: no*no

print("enter the numbers:")

value = list(map(int,input().split()))

sun = list(map(squar,value))

print("the squers is :",sun)
