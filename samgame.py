import random
value=random.randint(1,20)
won=False
wtp=True
while(wtp):
    print"hi ! I m thinking of a no.,can you guess it?"
    for tri in range(3):
        guess=int(raw_input("Enter a no: "))
        if(guess==value):
            won=True
            print"Congrats"
            break
        elif(tri<2):
                print"sorry! try again"
                print 3-tri-1,"tries left"
        if(won==False and tri==2):
            print"sorry ! you lost"
            print "NO. was:", value
    choice=str(raw_input("would you like to play again y/n "))
    if(choice=="n"):
        wtp=False
