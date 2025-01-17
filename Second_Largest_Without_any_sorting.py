def secondlargest(l):
    sl=lr=float('-inf')
    for i in l:
        if i>lr:
            sl=lr
            lr=i
        elif i>sl and lr!=i:
            sl=i

    return sl
    


if __name__=="__main__":
    n=int(input("Enter the limit:"))
    l=[]
    for i in range(n):
        l.append(int(input("Enter the elements:")))
    print(secondlargest(l))
