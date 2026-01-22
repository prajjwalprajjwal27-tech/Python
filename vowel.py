def vowel(ch):
    if ch in ["a","e","i","o","u"]:
        print("it is vowel")
    else:
        print("normal character")    


def main():
    print("enter the character ")
    value = input()
    Ret = vowel(value)
    print(Ret)        
if __name__=="__main__":
    main()


