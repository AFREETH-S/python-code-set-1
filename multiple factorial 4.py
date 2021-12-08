def factall(n):
    fact=1
    f=1
  
    
    for i in range(1,n+1):
        for j in range(1,i+1):
            fact=fact*j


    print("The multiplication of factorial {} of factorial is : {}".format(n,fact))
n=int(input("Enter a number to factorial all the lesser number: "))
factall(n)
