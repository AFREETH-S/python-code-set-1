def fact(n):
    fa=1
    for i in range(1,n+1):
        fa=fa*i
    print("the factorial of {} is {}".format(n,fa))
n=int(input("enter the number to factorized: "))
fact(n)
      
