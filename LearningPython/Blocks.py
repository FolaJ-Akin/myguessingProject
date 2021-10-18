name = input("Please enter your name: ")
# add int( to input( to return the data type as an integer not string :
# anything inputted that is returned as not an integer will leave an error
age = int(input("How old are you, {0}? ".format(name)))
print(name + " is " + str(age) + " years old!")
# crtl+/ to make everything highlighted into notes
if age < 18:
    print("Please come back in {0} years {1}".format(18 - age, name))
elif age == 25:
    print("Not only can you vote but you can also rent a car abroad")
    print("Please put an 'X' in the box")
else:
    print("You are old enough to vote {0}".format(name))
    print("Please put an 'X' in the box")
print()
print()

# Blocks
# for i in range(1,14):
#     print("{:2} squared is {:3} and cubed is {:>4}. {:2} the power of 4, is {:5} ".format(i,i**2,i**3,i,i**4))