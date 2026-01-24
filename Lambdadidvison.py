div = lambda no1 : no1 % 3 == 0 or no1 %5 == 0
print("enter the numbers ")
value = list(map(int,input().split()))
fun = filter(div,value)
print (list(fun))