name = input("Please enter you name:")
age = int(input("How old are you, {0}? ".format(name)))
print(name + " is " + str(age) + " years old!")
if "gloria" in name.casefold():
    print(" However, it says here on the system that Gloria is a yam but have a great day.")
elif age > 0:
    print("Have a wonderful day " + name + "!" )