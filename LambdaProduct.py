import functools

product = lambda x,y : x * y
print("enter the elements:")
value = list(map(int,input().split()))
fun = functools.reduce(product,value)
print(fun)