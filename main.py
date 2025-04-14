import random

computer=random.choice([-1,0,1])
yourDict= {"rock":1, "paper":0, "scissor":-1}
yourStr=(input("Enter your choice:"))
you= yourDict[yourStr]

reverseDict={1: "rock", 0: "paper", -1: "scissor"}

print(f"You've chosen {reverseDict[you]}")
print(f"Computer has chosen {reverseDict[computer]}")

if(you==computer):
    print("it's a draww! :(")

else:
    if(computer==1 and you==0):
        print("You win!")
    
    if(computer==1 and you==-1):
        print("computer win!")

    if(computer==0 and you==1):
        print("Computer win!")
    
    if(computer==0 and you==-1):
        print("You win!")

    if(computer==-1 and you==0):
        print("Computer win!")
    
    if(computer==-1 and you==1):
        print("You win!")

