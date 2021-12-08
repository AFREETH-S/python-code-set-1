def same_number(n):
    count=0
    index=0
    n.sort()
    while index<(len(n)-1):
        if (n[index]==n[index+1]):
            count+=1
            index=index+2
        else:
            index+=1
    print(count)
n=list(map(int,input("enter the numbers: ").split()))
same_number(n)
