def longestcommonprefix(l):
    l.sort(reverse=True)
    f=l[0]
    l=l[-1]
    m=[]
    for i in range(len(f)):
        if(f[i]==l[i]):
            m.append(f[i])
        else:
            return "".join(m)
        






if __name__=="__main__":
    n=int(input("Enter the limit:"))
    l=[]
    for i in range(n):
        l.append(input("Enter strings:"))
    print(longestcommonprefix(l))
