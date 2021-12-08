import math
def alternate(n):
    lis1=["I CAN ","I WILL "]
    if n%2!=0:
        a=math.floor(n/2)
        e=[lis1*a,lis1[0]]
        print(e)
    else:
        a=math.floor(n/2)
        
        print(string(e).replace("["," ").replace("]"," "))
n=int(input("enter the number: "))
alternate(n)
