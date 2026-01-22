import math
def fun(w):
    area = 0
    area = math.sqrt(w / math.pi)
    
    print("the area of circle is:",area)
def main():
    print("enter the radius")
    value = int(input()) 

    
    Ret = fun(value)
    print(Ret)
if __name__=="__main__":
    main()    