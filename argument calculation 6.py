def arg_calc(a1,a2,n):
    if n=='+':
        print( a1+a2)
    elif n=='-':
        print(a1-a2)
    elif n=='*':
        print( a1*a2)
    elif n=='/':
        print(a1/a2)
    else:
        print("check your operater ")
a1,a2=map(int,input().split(","))
n=input()
arg_calc(a1,a2,n)
