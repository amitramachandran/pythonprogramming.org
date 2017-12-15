#asking for their inputs
player1= raw_input("play ur turn:")
#player2= raw_input("play your turn:")
a=["rock","paper","scissor"]
import random
comp=random.shuffle(a)
for item in a:
    player2=item
print "comp :",player2
if player1==player2:
    print "replay"
elif player1==a[0] and player2=="scissor":
    print "player1 wins"
elif player1 == a[0] and player2 == "paper":
    print "comp wins"
elif player1==a[1] and player2=="rock":
     print "player1 wins"
elif player1==a[1] and player2=="scissor":
     print "comp wins"
elif player1==a[2] and player2=="paper":
    print "player1 wins"
elif player1==a[2] and player2=="rock":
    print "comp wins"






