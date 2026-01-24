def ChkNum(no):
    if no % 2 == 0:
        print("it is even:")
    else :
        print("it is odd :")

def main():
    print("enter the number :")
    value = int(input())
    ChkNum(value) 
if __name__=="__main__":
    main()    