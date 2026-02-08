# Initialize two sets for skill comparison
my_skills = {"Python", "Git", "SQL"}
job_requirements = {"SQL", "Docker", "Linux", "Git"}
print(id(my_skills))
# 1. .add() — Add a single unique element
my_skills.add("Django")
new_skills = my_skills
print(id(new_skills))

# 2. .discard() — Safe removal (does not raise an error if item is missing)
my_skills.discard("Java")

# 3. SET OPERATIONS (Mathematical logic):

# Union (|) — Combine all unique elements from both sets
all_skills = my_skills | job_requirements

# Intersection (&) — Find elements present in both sets
matching_skills = my_skills.intersection(job_requirements)
print(f"I match the requirements for: {matching_skills}")

# Difference (-) — Elements in the first set but not the second
missing_skills = job_requirements - my_skills
print(f"I need to learn: {missing_skills}")

# 4. .clear() — Remove all elements from the set
my_skills.clear()


# math example
first_plural = {1,2,3,4,5,6,7}
second_plural = {6,7,8,9,10}

union_plural = first_plural | second_plural
#union_plural = first_plural.union(second_plural)
print(union_plural)

intersection_plural = first_plural & second_plural
#intersection_plural = first_plural.intersection(second_plural)
print(intersection_plural)

difference_plural = first_plural - second_plural
#difference_plural = first_plural.difference(second_plural)
print(difference_plural)