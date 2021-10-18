import random
highest_number = 10
answer = random.randint(1, highest_number)
# print(answer)
print()
print("Please guess a number between 1 and " + str(highest_number))
guess = int(input("Type guess here:"))
# trys = ""
while guess is not answer:
    if guess == 0:
        print("Game over.")
        print("Please try again another time")
        break
    if guess < answer:
        print("Answer is too small, please guess again.")
    elif guess > answer:
        print("Answer is too big, Please guess again.")

    # trys = [trys + str(guess)]
    # print("numbers you have already guessed:")
    # print(trys)
    guess = int(input("Type guess here:"))

if guess == answer:
    print("You guessed it right! Congratulations")