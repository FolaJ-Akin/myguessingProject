# 'while' loops; as long as the condition is still true python we continue the loop until the condition becomes false
# 'While' example

for i in range(10):
    print("i is now {}".format(i))
print("*" * 25)

# 'while' loops are needed with an initialised variable to be stated
i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1  # increases i by the value 1
    # i = i + 1 is what i += 1 means
