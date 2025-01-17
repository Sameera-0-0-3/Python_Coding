def secondlargest(l):
    l.sort()
    return l[-2]

if __name__=="__main__":
    n=int(input("Enter the limit:"))
    l=[]
    for i in range(n):
        l.append(int(input("Enter elements:")))
    print(secondlargest(l))
