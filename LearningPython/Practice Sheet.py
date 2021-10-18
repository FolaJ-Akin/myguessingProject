# x = 5
# y = 7
# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is smaller than y")
# else:
#     print("x equals y")

# Challenge 47
# answer = 5
# print("Please guess a number between 1 and 10")
# guess = int(input("Type guess here:"))
# if guess == answer:
#     print("Congratulations, you guessed right the first time")
# else:
#     if guess > answer:
#         print("you guessed too high; try again! you have one more chance.")
#     else:
#         print("your guess was too low; try again! you have one more chance")
#     guess = int(input("Type your second guess here:"))
#     if guess == answer:
#         print(" you guess it correctly the second time, Well done!")
#     else:
#         print("oops! You guess incorrectly the second time!")
#         print("restart the game to try again!")

# Challenge 53
# name = input("Please enter your name?")
# age = input("{}, can you please enter your age?".format(name))
# if 30 >= int(age) >= 18:
#     print("Welcome to the Holiday!")
# else:
#     print("Sorry you won't be able to attend the holiday")
#     if int(age) > 30:
#         print("The age limit for this holiday is 30 years-old")
#     else:
#         print("please come back in " + str(18 - int(age)) + " years.")

# Code exercise 7
# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
# Capitals = ""
# for char in quote:
#     if char.isupper():
#         Capitals = Capitals + char
# print(Capitals)
# Use a for loop and an if statement to print just the capitals in the quote above.

# challenge 10
# for i in range(1,21):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     print(i)

# Challenge 12
number = 10
multiplier = 9
answer = 0

# # add your loop after this comment
# while True:
#     answer += (multiplier * number )
#     print(answer)
#     break

# Challenge 80
choice = "-"

while True:

    if choice in ("12345"):
        print("The option you have opted for is: {}".format(str(choice)))
    elif choice == "0":
        print("Exit")
        break
    else:
        print("Please choose your option from the list below:")
        print("\toption 1 is Learn python")
        print("\toption 2 is Go back university and do master")
        print("\toption 3 is work full-time in manchester")
        print("\toption_4 is Apply for J.P morgan Grad Job")
        print("\toption_5 is Wait till next graduate job intake")
        print("\toption_0 is Exit")
    choice = input("Please type your choice here:")