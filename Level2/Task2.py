import random
print("Enter a range in which you want to play the Number Guessing game:")
a=int(input("Enter lower limit:"))
b=int(input("Enter upper limit:"))
n = random.randint(a,b)
while True:
    guess = int(input("Enter your guess number: "))
    if guess < n:
        print("Too low! Try again.")
    elif guess > n:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number:{n}.")
        break