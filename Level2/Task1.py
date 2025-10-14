import random 
num=random.randint(1,100)
while True:
    guess = int(input("Guess a number between 1 and 100:"))
    if guess<num:
        print("too low! Try again.")
    elif guess>num:
        print("too high! Try again.")
    else:
        print(f"Congratulation! You got the number{num}")
        break