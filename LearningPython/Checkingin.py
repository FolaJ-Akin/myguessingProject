# 'in' and 'not in' example
activity = input("what would you like to do today?")

if "cinema" not in activity.casefold():
    print("I'll rather go to the cinema today")
else:
    film = input("What film would you like to watch?")
    if "black widow" not in film.casefold():
        print("I don't really want to watch that right now")
    else:
     print("That sounds great! lets go.")