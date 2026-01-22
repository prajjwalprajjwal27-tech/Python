def fun(w,l):
    area = 0
    area = w*l

    print("the area of rectangle is:",area)
def main():
    print("enter the width")
    value1 = int(input()) 

    print("enter the length")
    value2 = int(input()) 
    Ret = fun(value1,value2)
    print(Ret)
if __name__=="__main__":
    main()    