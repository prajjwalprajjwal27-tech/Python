char = lambda no : len(no)>5
print ("enter the  words")
value = input().split()
fun = list(filter(char ,value))
print(fun)

