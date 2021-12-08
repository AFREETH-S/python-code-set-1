def check_list(n,m):

    lis1=[]
    for i in n+m:
        lis1.append(i)

    lis1.sort()
    compare=[]
    for i in range(min(lis1),max(lis1)+1):
        compare.append(i)
    
    i=0
    y=0
    no=0

    while i<=max(lis1)-1:
        if lis1[i]==compare[i]:
            y=i+1
            i=i+1
            
        else:
            no=i+1
            i=i+1
    if no>0:
        print("not consecutive ")
    else:
        print("consecutive ")
            
            
        
n=list(map(int,input("enter 1st list: ").split()))
m=list(map(int,input("enter 2nd list: ").split()))
check_list(n,m)
