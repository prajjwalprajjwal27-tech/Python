even = lambda x : x % 2 ==0
print("enter the list of numbers")
no = list(map(int,input().split()))
fun = list(filter(even,no))
print (len(fun),"the even numbers ")