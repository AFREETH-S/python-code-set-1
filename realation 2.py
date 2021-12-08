def reala(n):

    father     ="Luke, I am your father"
    sister     ="Luke, I am your siser"
    brotherlaw ="Luke, I am your brother in law"
    droid      ="Luke, I am your droid"

    if n=="darth vader" or n=="Darth Vader":
        print(father)
    elif n=="leia" or n=="Leia":
        print(sister)
    elif n=="han" or n=="Han":
        print(brotherlaw)
    elif n=="r2d2" or n=="R2D2":
        print(droid)

n=input("enter your name to find the realation with luke: ")
reala(n)
