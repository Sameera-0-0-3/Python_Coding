def fibonacci(n):
    a=0
    b=1
    l=[0,1]
    for i in range(2,n):
        c=a+b
        l.append(c)
        a=b
        b=c
    return " ".join(map(str,l))




if __name__=="__main__":
    n=int(input("Enter the limit:"))
    print(fibonacci(n))
