def reversesentence(s):
    l= s.split(" ")
    print(l)
    l.reverse()
    return " ".join (l)




if __name__=="__main__":
    s=input("enter the sentence to be reversed:")
    print(reversesentence(s))
