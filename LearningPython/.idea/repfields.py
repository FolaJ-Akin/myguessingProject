age = 24
# using the string function - str() - changes an interger data type into a string
print("My age is " + str(age) + " years")
#alternatively
#the value {0} is replaced by the first value in the format list
print("My age is {0} years".format(age))
# long lines are avoided so split over two lines with shift button
# replacement fields are replaced by the values that appear in the "dot format method call"
# the first value replaces 0 then 1 and so on till 7
# Using the Dot format method call
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))
print()

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}"""
.format(28, 30, 31))