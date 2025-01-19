def thirdlargest(l):
    t=float("-inf")
    s=float("-inf")
    f=float("-inf")
    for i in l:
        if i>f:
            t=s
            s=f
            f=i
        elif i>s and i!=f:
            t=s
            s=i
        elif i>t and i!=s:
            t=i

    return t            



if __name__=="__main__":
    n=int(input("Enter the limit:"));
    l=[]
    for i in range(n):
        l.append(int(input("Enter element:")));
    print(thirdlargest(l))
