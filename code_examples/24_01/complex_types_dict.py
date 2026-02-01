# Initialize a student dictionary

empty_dictionary = {}

student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}

# 1. .get() — Safe retrieval (returns None or a default value instead of crashing if key is missing)
email = student.get("email", "No email provided")
print(f"Email: {email}")

# 2. .update() — Add or modify multiple fields at once
student.update({"age": 21, "city": "Kyiv"})

# 3. .keys(), .values(), .items() — Viewing content
print(student.keys())    # Returns a view of all keys
print(student.values())  # Returns a view of all values
print(student.items())   # Returns a list-like view of (key, value) tuples

# 4. .pop() — Remove a specific key and return its value
removed_course = student.pop("course")
print(f"Removed course: {removed_course}")

# 5. .setdefault() — Adds a key with a value only if the key does not already exist
student.setdefault("status", "Active")