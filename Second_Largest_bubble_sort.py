def secondlargest(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if (l[j]>l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]
    return l[-2]

if __name__=="__main__":
    n=int(input("Enter the limit of list:"))
    l=[]
    for i in range(0,n):
        l.append(int(input("Enter elements:")))

    print(secondlargest(l))
