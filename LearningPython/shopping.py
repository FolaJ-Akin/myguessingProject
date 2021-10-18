# 'continue' and 'break' example
# list '[]'
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)
# continue causes everything else in the loop to be skipped
for item in shopping_list:
    if item == "spam":
        continue
    print("Buy " + item)
print()
print()
# break cause to completly break from the loop, anything after break item will not be recorded
for item in shopping_list:
    if item == "spam":
        break
    print("Buy " + item)