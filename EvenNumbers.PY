def even(n):
        for i in range(2, n+1, 2):
         print(i)




def main():
    print("enter the number :")
    value = int(input())
    Ret = even(value)
    print(Ret)

    

if __name__=="__main__":
    main()