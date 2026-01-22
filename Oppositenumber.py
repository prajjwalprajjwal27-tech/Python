def opposite(n):
    q = 0 
    while n > 0:
        p = n % 10
        q = (q *10)+p
        n //=10
    return q




def main():
    print("enter the number")
    value = int(input())
    Ret = opposite(value)
    print (Ret)



if __name__=="__main__":
    main()        