def sum(no):
    ans = 0
    fun = 0
    gun = 0

    ans  = no +1
    fun = ans *no
    gun = fun /2

    return gun




def main():
    print("enter the number:")
    value = int(input())
    Ret = sum(value)

    print (Ret)


if __name__=="__main__":
        main()