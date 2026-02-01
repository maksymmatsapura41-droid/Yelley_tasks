# Initialize a tuple of test scores
grades = (10, 12, 8, 10, 9, 10, 8, 8)
grades_list = [10, 12, 8, 10, 9, 10]


val_1 = True
grade = (True, val_1)
print(grade)


def simple_function(a,b):
    return a+b

simple_function(7, 4)

# 1. .count() — Count how many times an element appears
ten_count = grades.count(10)
print(f"Number of 10s: {ten_count}") # Output: 3

# 2. .index() — Find the position of the first occurrence of an element
index_of_eight = grades.index(8)
print(f"The grade 8 is at index: {index_of_eight}") # Output: 2



# Practical usage: Tuple Unpacking
point = (4, 5, 4, 2, 5, 6)
x, y, *other_values= point  # Assigns 4 to x and 5 to y

print(x, y, other_values)

tuple1 = ("a", "b")
tuple2 = (1, 2)
combined = tuple1 + tuple2  # Output: ('a', 'b', 1, 2)


tuple3 = (1, 2, 3)
tuple4 = tuple3 * 2
# str_1 = "hey"
# print(str_1 * 3)
print(tuple4)
print(tuple4[4:])

grades_1 = (10, 12, 8, 10, 9, 10, 8, 8)
grades_list_1 = [10, 12, 8, 10, 9, 10]

print(grades_1[1:4])
#12, 8, 10


print(grades_1[2:5:2])

# tuple[start:stop:step]
# start - included
# stop - stop