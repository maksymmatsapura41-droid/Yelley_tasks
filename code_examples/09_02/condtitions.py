# result = 5 > 7
# print(result)
# print(type(result))
# age = 18
# if age >= 21:
#     print("You can enter and order anything.")
# name = "John"
#
# # simple logical check
# if age == 21:
#     print("You can enter and order anything.")
#
# if age != 21:
#     print("You can enter and order anything.")
#
# if age < 21:
#     print("You can enter and order anything.")
#
# if age <= 21:
#     print("You can enter and order anything.")
#
# if age <= 21 and name == "John":
#     print("You can enter and order anything.")
#
# if age <= 21 or name == "John":
#     print("You can enter and order anything.")
#
# if age >= 21:
#     print("You can enter and order anything.")
# elif age >= 18:
#     print("You can enter, but no alcohol!")
# else:
#     print("You are too young to enter.")
#
# # using in operator
# banned_users = {"admin_bot": 1, "spammer_99": 2, "troll_face": 3}
# current_user = "spammer_99"
#
# if current_user in banned_users:
#     print("Access Denied!")
# else:
#     print("Welcome to the forum.")
#
# str_1 = 'Hello World'
# if "i" in str_1:
#     print("Hello World!")
#
#
# shopping_cart = [] # An empty list (it is naturally False)

#not True == False

#not False == True

print(not False)

x = 5

if not x > 6:
    print("a")



# if shopping_cart:
#     print("This list is not empty.")
#
# if not shopping_cart:
#     print("Your cart is empty. Keep shopping!")
# else:
#     print(f"You have {len(shopping_cart)} items in your cart.")
#
#
# # Multiple Conditions (Complex Logic)
#
# has_ticket = True
# is_vip = False
# age = 25
#
# # If they have a ticket OR they are VIP, AND they are over 18
# if (has_ticket or is_vip) and age >= 18:
#     print("Entry permitted.")
# else:
#     print("Entry refused.")
#
# # Nested Conditions
#
# is_authenticated = True
# has_permission = False
#
# if is_authenticated:
#     if has_permission:
#         print("Editing document...")
#     else:
#         print("Error: You don't have permission to edit.")
# else:
#     print("Error: Please log in first.")
#
# user = ["email", "picture", "bio"]
#
# if "email" in user:
#     print("send a letter to the user")
# if "picture" in user:
#     print("Check picture size")
#
# if "email" in user:
#     print("send a letter to the user")
# elif "picture" in user:
#     print("Check picture size")
#
#
# # list_of_grades = ["A", "B", "C"]
# grade = input("Enter the grade: ")
#
# if grade == "A":
#     print("Your grade is A.")
# elif grade == "B":
#     print("Your grade is B.")
#
#
