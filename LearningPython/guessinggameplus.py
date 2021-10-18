# if elif else game test

answer = 5

print()
# print("Please guess a number between 1 and 10")
# guess = int(input("Type guess here:"))
# if guess < answer:
#     print("Answer is too small, please guess again. You have one more chance")
#     guess = int(input("Type your second guess here:"))
#     if guess == answer:
#         print("You guess it right the second time! Congratulations")
#     elif guess is not answer:
#         print("you guessed wrong again, too bad!")
#         print("Please restart game")
# elif guess > answer:
#     print("Answer is too big, Please guess again. You have one more chance")
#     guess = int(input("Type your second guess here:"))
#     if guess == answer:
#         print("You guessed it right the second time! Congratulations")
#     else:  # n.b the difference when using elif versus else
#         print("you guessed wrong again, too bad!")
#         print("Please restart game")
# else:
#     print("You guessed it right the first time! Congratulations")
# not equal is !=


# The Game has been optimised by using 'if' and 'else' statements in series
print("Please guess a number between 1 and 10")
guess = int(input("Type guess here:"))
if guess is not answer:
    if guess < answer:
        print("Answer is too small, please guess again. You have one more chance")
    else:
        print("Answer is too big, Please guess again. You have one more chance")
    guess = int(input("Type your second guess here:"))
    if guess == answer:
        print("You guess it right the second time! Congratulations")
    else:
        print("you guessed wrong again, too bad!")
        print("Please restart game")
else:
    print("You guessed it right the first time! Congratulations")