def divisible(no):
    if (no % 3 == 0) and (no %5 == 0 ):
        print("divisable by 3 and 5")

     
    else : 
        print("not devisible this number")

value = 0
print("enter the number")
value = int(input())

divisible(value)

