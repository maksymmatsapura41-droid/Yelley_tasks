# Initialize a student dictionary

empty_dictionary = {}

set_variable = {1,2,2,3}

student = {
    "name": "John",
    "age": 20,
    "course": "Python",
    "email": "example@gmail.com",
}

# print(student["age"])

# 1. .get() — Safe retrieval (returns None or a default value instead of crashing if key is missing)
email = student.get("email1", "No email provided")
# print(f"Email: {email}")
#
# # 2. .update() — Add or modify multiple fields at once
student.update({"age": 21, "city": "Kyiv"})
# print(student)
#
# # 3. .keys(), .values(), .items() — Viewing content
# print(student.keys())    # Returns a view of all keys
# print(student.values())  # Returns a view of all values
# print(student.items())   # Returns a list-like view of (key, value) tuples
#
# # 4. .pop() — Remove a specific key and return its value
removed_course = student.pop("course")
print(f"Removed course: {removed_course}")
print(student)
#
# # 5. .setdefault() — Adds a key with a value only if the key does not already exist
student.setdefault("age", 25)
# student.update({"age": 25})


student["age"] = 123

print(student)


## -----
# Add more straight example for setdefault  method

player_stats = {"nickname": "DragonSlayer", "level": 10}

player_stats.setdefault("level", 1)
player_stats.setdefault("health", 100)
player_stats.setdefault("mana", 50)

print(player_stats)

# ------- update
player_stats = {"nickname": "DragonSlayer", "level": 10}

player_stats.update({
    "level": 1,
    "health": 100,
    "mana": 50
})

print(player_stats)