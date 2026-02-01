numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# Get items from index 2 to 5 (not including 5)
middle_part = numbers[2:5]
# Result: [20, 30, 40]

# Get the first 3 items (starts from index 0 by default)
first_three = numbers[:3]
# Result: [0, 10, 20]

# Get all items from index 6 to the very end
last_part = numbers[6:]
# Result: [60, 70, 80, 90]

# Get every second item in the list (using step)
every_second = numbers[::2]
# Result: [0, 20, 40, 60, 80]

# ==================================
# With str

text = "Python Programming"

# Slice from index 0 to 6
word1 = text[0:6]
# Result: "Python"

# Slice using negative indices (last 7 characters)
word2 = text[-11:]
# Result: "Programming"

# Reverse the entire string using a negative step
reversed_text = text[::-1]
# Result: "gnimmargorP nohtyP"


'''
obj[start:stop]	Items from start through stop-1
obj[start:]	Items from start through the rest of the array
obj[:stop]	Items from the beginning through stop-1
obj[:]	A copy of the whole array
obj[::step]	Every step-th item
obj[::-1]	All items, but in reverse order
'''