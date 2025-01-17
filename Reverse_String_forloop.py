def reversestring(s):
    ns=""
    for i in s:
        ns=i+ns
    return ns
if __name__=="__main__":
    s=input("Enter the string:")
    print(reversestring(s))
