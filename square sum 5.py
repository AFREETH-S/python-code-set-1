def square_sum(n):
    total=0
    for i in n:
        total+=i*i
    print(total)
n=list(map(int,input("enter the numbers: ").split()))
square_sum(n)
