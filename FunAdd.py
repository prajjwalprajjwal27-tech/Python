def add(no1,no2):
    ans = 0
    ans = no1 + no2 
    return ans
def main():
    print("enter the first number:")
    value1 = int(input())

    print("enter the second number:")
    value2 = int(input())

    Ret  = add(value1,value2)
    print("Additiom of number:",Ret)
    
if __name__=="__main__":
    main()   
