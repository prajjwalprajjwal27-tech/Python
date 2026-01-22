def sum(no1,no2):
    add = no1 + no2
    sub = no1 - no2
    multi = no1 * no2
    divid = no1 / no2
     
    return add,sub,multi,divid
    


def main():
    print("enter the first number")
    value1 = int(input())

    print("enter the second number")
    value2 = int(input())

    add,sub,multi,divid = sum(value1,value2)

    
    print("addition of two numbers:",add)
    print("substraction of two numbers:",sub)
    print("multiplaction  of two numbers:",multi)
    print("division of two numbers:",divid)


if __name__=="__main__":
    main()    
