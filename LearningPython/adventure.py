available_exits = ["north", "east", "south", "west"]
# 'while' loops are used when you can't determine in advance how many times you need to loop: i.e reading data in a
# stream; till there is no more left
# for loops are used with a pre-determined number of variables
chosen_exit = ""  # empty string # initialised variable
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ").casefold() # casefold after 'please choose a direction' variable turns every 'input' inputted in lowercase
    if chosen_exit.casefold() == "quit":  # casefold after 'chosen_exit' variable turns every 'input' inputted in lowercase
        print("Game over")
        break
else: # the else cause will only be excuted if the while loop terminates normally
    print("Aren't you glad you got out of there!")
