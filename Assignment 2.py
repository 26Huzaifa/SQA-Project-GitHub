#Q1.

p1 = input("Choose from rock, paper or scissors: ")
p2 = input("Choose from rock, paper or scissors: ")
r = "rock"
p = "paper"
s = "scissors"
q = "quit"
if p1 == r and p2 == p:
    print("Congratulations! Player 2 has won!")
elif p1 == r and p2 == s:
    print("Congratulations! Player 1 has won!")
elif p1 == p and p2 == r:
    print("Congratulations! Player 1 has won!")
elif p1 == p and p2 == s:
    print("Congratulations! Player 2 has won!")
elif p1 == s and p2 == r:
    print("Congratulations! Player 2 has won!")
elif p1 == s and p2 == p:
    print("Congratulations! Player 1 has won!")
elif p1 == p2:
    print("It's a draw! Try Again")
    p1 = input("Choose from rock, paper or scissors: ")
    p2 = input("Choose from rock, paper or scissors: ")
elif p1 == q or p2 == q:
    print("Game ended")
else:
    print("Play again")
    p1 = input("Choose from rock, paper or scissors: ")
    p2 = input("Choose from rock, paper or scissors: ")

#---------------------------------------------------------------------

#Q2.

a = int(input("Enter the input in seconds: "))
d = a//86400
h = (a%86400)//3600
m = ((a%86400)%3600)//60
s = (((a%86400)%3600)%60)
print("The days, hours, minutes and seconds(d:h:m:s) are as follows:")
print(f"{d}:{h}:{m}:{s}")

#---------------------------------------------------------------------
    
