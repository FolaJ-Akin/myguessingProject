print("The bear's are going on tour.")
print('fola' + ' loves' + ' games')
print('fola said "I am here for a good time not a long time". ')
warning = 'Run as quick as you can'
name = 'Fola'
# input function displays text provided in it and then waits for text to be entered at the keyboard
print(warning + ' ' + name)

age = 22
print(age)
# Examine what type of value a variable is by using the print(type())function
print(type(warning))
print(type(age))
# str - string
# int - integer

age = 21
print(age)
print(type(age))
# we have rebound the label "age"  to the string value "two years"
age_in_words = "2 years"
# F-string
# print(name + " is " + age + " years old") would give an error because of age variable: "TypeError: can only concatenate str (not "int") to str"
# Instead we add f-string
print(name + f" is {age} years old")
# more examples of f-string
print(f"Pi is approximately {22 / 7:12.50f}")
print()
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
# however this won't work on python versions earlier than 3.6
