def perfect(n):
    if n <= 0:
        return False
    p = 0
    for i in range(1,n):
        if n % i == 0:
            p  += i

    return p==n



def main():
    print("enter the number")
    value = int(input())
    Ret = perfect(value)
    if Ret :
        print(value,"is a perfect number:")
    else:
        print(value, "it is not perfect value:")    



if __name__=="__main__":
    main()        
    