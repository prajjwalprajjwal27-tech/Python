

def digitsum(n):
    p = list(map(int, str(n)))
    ans = sum(p)
    return ans




def main():
    print("enter thr number:")
    vallue = int(input())
    Ret = digitsum(vallue)
    print(Ret)

if __name__=="__main__":
        main()