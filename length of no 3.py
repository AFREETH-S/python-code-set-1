def lenofno(n):
    if n==0:
        print("1")
    else:
        l=0
        while n!=0:
            n=n//10
            l=l+1
        print(l)
n=int(input("enter the number to count the digits: "))
lenofno(n)
