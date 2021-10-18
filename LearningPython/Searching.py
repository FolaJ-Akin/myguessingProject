shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# 'break' is useful in searching list so that python can end search once an item is found
item_to_find = "spam"
found_at = None # code needs to be initialised
# for loop searching for an index list
# len() lets us know how many items in a list
for index in range(len(shopping_list)):  # len(shopping_list)) returns the value 6; so we are indexing in range(6)
    if shopping_list[index] == item_to_find:
        found_at = index
        break
if found_at is not None:
    print("item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))

# better code
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))