def palindeome(n):
    sum = n
    q = 0 
    

    while n > 0:
        p = n % 10
        q = (q *10)+p
        n //=10
    if sum ==  q:
        print(f"{sum} is palindeoms number")
    else:
        print("it is not palindeoms number ")    




def main():
    print("enter the number")
    value = int(input())
    Ret = palindeome(value)
    print (Ret)



if __name__=="__main__":
    main()        