def sun(a):
    ans = 0
    ans  = ("*" * a)
    return ans

def main():
    
    No = int(input("enter the number to primt a stars "))
    Ret = sun(No)
   
    print (Ret)

if __name__=="__main__":
    main()