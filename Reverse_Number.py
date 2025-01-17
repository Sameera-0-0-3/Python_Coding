def reversenum(num):
    s=0
    while(num>0):
        r=num%10
        s=s*10+r
        num=num//10
    return s
#it can be also done using string methods
#an integer can be converted into list only after converting it into string then into list


if __name__=="__main__":
    n=int(input("Enter a number:"))
    print(reversenum(n))
