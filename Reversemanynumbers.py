def more(n):
    for i in reversed(range(1,n+1)):
        print (i)


def main():
    print("enter the number")
    value = int(input())
    Ret = more(value)

if __name__=="__main__":
    main()
