def gun(a):
    for i in range(a):            
        for j in range(a):        
            print("*",end=" ") 
        print()                   




def main():
    No = int(input("enter the number to print a stars "))
    gun(No)
if __name__=="__main__":
    main()