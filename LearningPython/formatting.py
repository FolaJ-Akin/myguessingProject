# not expected to know how to write for statement yet
# n.b 4 spaces before print on line 4
for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))
# adding formatting to the width
print()
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
# {0:2} prints with a width of 2 characters  and {2:4} a width of 4 because the values have up to 4 figures
# To left align we place a < after the colon like so ':<'
# we use the caret symbol ^ to center align; ':^'
print()

print(" Pi is approximately {0:12}".format(22 / 7))  # default format of 15 decimals
print(" Pi is approximately {0:12f}".format(22 / 7))  # using a floating-point value using the f gives 6 decimals
print(
    " Pi is approximately {0:12.50f}".format(22 / 7))  # 12 digits value however python overrides for the floating point
print(" Pi is approximately {0:52.50f}".format(22 / 7))  # 52 figures
print(" Pi is approximately {0:62.50f}".format(22 / 7))  # 62 figures
print(" Pi is approximately {0:<72.50f}".format(22 / 7))  # 72 figures
print(" Pi is approximately {0:<72.54f}".format(22 / 7))  # 72 figures with 54 decimal places
