def min(n):
    if n >= 75 :
        print("Distinction")
    if n >=60:
        print("First class")
    if n >=50:
        print("Second class")
    if n <= 50:
        print("fail")
     

def main():
    print("Enter the marks")  
    no = float(input()) 
    Ret = min(no)     
if __name__=="__main__":
    main()  
