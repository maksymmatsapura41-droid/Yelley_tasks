# Range function
# range (start, stop, step)
# range (0, n-1, 1)
print(range(5))
print(list(range(5)))
print(list(range(2, 6)))
print(list(range(0, 10, 2)))
print(list(range(5, 0, -1)))

# example with list
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)

# example with list when you need indexes
for x in range(len(fruits)):
    print(f"index {x}: {fruits[x]} fruits")
    # index 0: apple
    # index 1: banana
    # index 2: cherry

# # example with range
# for x in range(5):
#     print(x)

#
# example of while loop
count = 1

while count <= 5: # Here should be condition similar to the statement if
    count = count + 1
    print(count)
    count = count + 1  # This is very important!

# # example with break
# for x in range(5):
#     if x == 2:
#         break
#     print(x)
#
# # examples with continue
# for x in range(5):
#     if x == 2:
#         continue
#     print(x)