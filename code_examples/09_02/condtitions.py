result = 5 > 7
print(result)
print(type(result))


# simple logical check
age = 18
if age >= 21:
    print("You can enter and order anything.")
elif age >= 18:
    print("You can enter, but no alcohol!")
else:
    print("You are too young to enter.")

# using in operator
banned_users = {"admin_bot", "spammer_99", "troll_face"}
current_user = "spammer_99"

if current_user in banned_users:
    print("Access Denied!")
else:
    print("Welcome to the forum.")

# Checking if a Collection is Empty

shopping_cart = [] # An empty list

if not shopping_cart:
    print("Your cart is empty. Keep shopping!")
else:
    print(f"You have {len(shopping_cart)} items in your cart.")


# Multiple Conditions (Complex Logic)

has_ticket = True
is_vip = False
age = 25

# If they have a ticket OR they are VIP, AND they are over 18
if (has_ticket or is_vip) and age >= 18:
    print("Entry permitted.")
else:
    print("Entry refused.")


# Nested Conditions

is_authenticated = True
has_permission = False

if is_authenticated:
    if has_permission:
        print("Editing document...")
    else:
        print("Error: You don't have permission to edit.")
else:
    print("Error: Please log in first.")