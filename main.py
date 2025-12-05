# Festival Inventory Disaster – Real‑World Python Collections Challenge
# Scenario
# You are hired as the Data Assistant for the Chicago Fall Music & Food Festival.
# The festival opens in 3 hours, but the digital system has scrambled the inventory lists, vendor data, and safety rules. Your job is to fix the data using Python lists, sets, and tuples.
# If you fail, the festival cannot legally open.

# Starting Data
foods = ["pizza", "tacos", "bbq", "tacos", "sushi", "corn", "bbq", "ice cream"]
stages = ("Main Stage", "Hip-Hop Zone", "Jazz Corner", "Indie Alley")
restricted = {"glass bottles", "weapons", "alcohol", "alcohol"}
attendance = [120, 130, 125, 145, 150, 148, 155, 160, 158, 162]


# Task 1 — Clean the Food Vendor List
    # 1. Remove duplicates while keeping only the first occurrence.

food2 = list(dict.fromkeys(foods))
# print(food2)

    # 2. Add "ramen" and "fried rice".

food2.append("ramen")
food2.append("fried rice")
# print(food2)

    # 3. Insert "smoothies" at index 2.
food2.insert(2, "smoothies")
# print(food2)

    # 4. Sort the list alphabetically.

food2.sort()
# print(food2)

    # 5. Print the final vendor list.

print(food2)

#Task 1.5 
    # combine all the list into a nested list called festival_data

festival_data = (food2, stages, restricted, attendance)

    #print out the new nested list(use a for loop to print each item on a new line)



for sublist in festival_data:
    for item in sublist:
        print(item, end=' ')                             # Print the item, followed by a space to keep items on the same line
    print()                                              # Print a newline character after each sublist is finished, moving to the next line for the next sublist


# Task 2 — Stage Map
    # 1. Print the second stage.

print(stages[1])

    # 2. Print the last two stages.

print(stages[-2:])

    # 3. Convert the tuple into a list and add "Rock Arena".

stages = list(stages)
stages.append("Rock Arena")

    # 4. Convert it back into a tuple.

stages = tuple(stages)

    # 5. Print the updated tuple.

print(stages)


# Task 3 — Restricted Items

restricted = {"glass bottles", "weapons", "alcohol", "alcohol"}

    # 1. Add "fireworks".

restricted.add("fireworks")

    # 2. Try adding "weapons" again.

restricted.add("weapons")

    # 3. Remove "alcohol".

restricted.remove("alcohol")

    # 4. Check if "glass bottles" is still restricted.


item_to_check = "glass bottles"

if item_to_check in restricted:
    print(f"{item_to_check} is in the list.")
else:
    print(f"{item_to_check} is not in the list.")

    # 5. Print the final restricted set.

print(restricted)


# Task 4 — Attendance Analysis

attendance = [120, 130, 125, 145, 150, 148, 155, 160, 158, 162]

    # 1. Print the first three hours.

print(attendance[0:3])

    # 2. Print the last hour.

print(attendance[-1])

    # 3. Print every 2nd hour.

every_sec_num = attendance[::2]
print(every_sec_num)

    # 4. Remove the 5th hour using pop().

attendance.pop(4)   
# print(attendance)

    # 5. Add five projected values using extend(range(...)).


# Define the start of your predicted values.
# For example, if you want to add 40, 41, 42, 43, 44
start_value = 170

# The range function generates numbers up to (but not including) the stop value.
# To get 5 values starting from start_value, the stop value will be start_value + 5.
attendance.extend(range(start_value, start_value + 5))

# print(attendance)

    # 6. Delete every 3rd value using del attendance[::3].

# del numbers[start:stop:step]
# Start at index 2 (the third item), go to the end, step by 3
del attendance[2::3]
# print(attendance)

  # 7. Print the length and cleaned list.

att_len = len(attendance)
print(att_len)


# Task 5 — Festival Master List
    # 1. Convert vendors, restricted set, and stages into lists.

food_list = list(food2)
restricted_list = list(restricted)
stages_list = list(stages)

    # 2. Combine everything into festival_data.

festival_data_list = (food_list, restricted_list, stages_list)

    # 3. Print: total items, first 10, last 10.

total = len(festival_data_list)
print(f"Total: {total}") 

    # 4. Remove duplicates.

# fest_data_list = list(set(festival_data_list))
# print(fest_data_list) 


    # 5. Print final cleaned festival_data.

print(festival_data_list)

# Extension
# Write a function festival_search(item) that returns True/False if item appears in festival_data.
