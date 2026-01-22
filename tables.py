def table(no):
    
    for i in range(1,11):
        print(no*i)
    


def main():
    value = 0
    print("table number :")
    value = int(input())
    Ret = table(value)
    print(Ret)

    

if __name__ == "__main__":
    main()                