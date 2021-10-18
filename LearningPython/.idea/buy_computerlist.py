available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mousemat",
                   "DVD drive"
                   ]
valid_choies = []
for i in range(1, len(available_parts)+1):
    valid_choies.append(str(i))
print(valid_choies)
current_choice = "-"
computer_parts = []

while current_choice != '0':
    if current_choice in valid_choies:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    else:
        print("please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))
    current_choice = input()

print(computer_parts)