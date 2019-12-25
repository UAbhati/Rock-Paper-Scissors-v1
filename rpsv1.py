LIST = ["ROCK","PAPER","SCISSORS"]
print("ROCK.....")
print("PAPER.....")
print("SCISSORS.....")
print("Let's Start the Game")
player1 = input("###Player 1 choice : ")
player1 = player1.upper()

print("*********No Cheating**********\n" * 30)

player2 = input("###Player 2 choice : ")
player2 = player2.upper()
if player1 == player2:
    print("It's a Tie!, Both of you have same choices")
elif player1 == "ROCK" and player2 == "PAPER":
    print("Player 2 WINS!")
elif player1 == "ROCK" and player2 == "SCISSORS":
    print("Player 1 WINS!")
elif player1 == "SCISSORS" and player2 == "PAPER":
    print("Player 1 WINS!")
elif player1 == "SCISSORS" and player2 == "ROCK":
    print("Player 2 WINS!")
elif player1 == "PAPER" and player2 == "ROCK":
    print("Player 1 WINS!")
elif player1 == "PAPER" and player2 == "SCISSORS":
    print("Player 2 WINS!")
else :
    print("You have not enter a valid choice")
