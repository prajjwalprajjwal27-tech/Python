def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    print("enter the number")
    vallue =int(input())
    Ret = factorial(vallue)
    print (Ret)



if __name__=="__main__":
    main()



