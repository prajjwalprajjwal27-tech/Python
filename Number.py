def fun(a):
    if a %5 == 0:
        return True
    else:
        return False
    
def main():
    No = int(input("enter the number"))
    Ret = fun(No)
   
    print (Ret)

if __name__=="__main__":
    main()
