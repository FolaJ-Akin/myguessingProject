#                   1
#         012345678901234
parrot = "Norwegian Blue"
#         432109876543210
#            -1
# Python counts character values from 0 not 1
print(parrot)

print(parrot[3])  # [with a number] after the string, prints the character value
print(parrot[9])
# Indexing
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

# Negative indexing
print('clear')
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()
print("New section")
print()
# Splicing

# 012345678901234
# Norwegian Blue

print(parrot[0:6])  # Norweg - ans // Nb last character isn't included in the section splice
# i.e [0:6] splices from the 0th Character to the 5th character (6th character is not included)
print(parrot[:9])  # if an initial character is not provided then it assumed to be thr 0th Character
print(parrot[10:14])
print(parrot[10:])  # End value for slice isn't provided however python assumes it to be the last character in the
# string
print()
print()

print(parrot[:6])
print(parrot[6:])
print(parrot[:6] + parrot[6:])  # Sliced strings can be added to together

print(parrot[:])  # useful for lists

# Negative Splicing
print()
print()
# 432109876543210
# Norwegian Blue

print(parrot[-4:-2])
print(parrot[-4:12])

# Step Slicing

print(parrot[0:6:2])  # Nre-ans starts from slice from 0th, to 6th character in steps of 2
print(parrot[0:6:3])  # Nw-ans  starts from slice from 0th, to 6th character in steps of 3

print("test question 8")
print()
#                                           -1
#       012345678901234567890123456789012345678
data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(type(data))
print(data[::5])
print(data[1:5])
print(data[0:-1:5])
print(data[:-1:5])