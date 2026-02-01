import Arithmetic
 
def gun(A,B):
    print("Addition of two numbwers :",Arithmetic.add(A,B)) 
    print("Substractionof two numbwers :",Arithmetic.sub(A,B)) 
    print("Division of two numbwers :",Arithmetic.Div(A,B)) 
    print("Multiplaction of two numbwers :",Arithmetic.Multi(A,B)) 

def main():
    print("enter the first number:")
    value1 = int(input()) 
    print("enter the second number:")
    value2 = int(input())      

    Ret = gun(value1,value2)
    return Ret
if __name__=="__main__":
    main()