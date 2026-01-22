def factor(n):
    
    p =[]

    for i in range(1,n+1):
        if  n % i == 0:
            p.append(i)
    return p
     

def main():
    print("enter thr number")
    value = int(input())
    Ret = factor(value)
    print("factor of value:",Ret)

if __name__=="__main__":
    main()    
