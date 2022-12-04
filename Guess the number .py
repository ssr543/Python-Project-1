import random
r=random.randint(1,20)

while (True):

    a=int(input("GUESS"))
    if (a>r):
        print ("Try smaller")
    elif (a<r):
        print ("Try greater")
    else:
        print ("Congrats! you've guessed it correct.")
        break ;
