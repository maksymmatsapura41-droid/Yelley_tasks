# Initialize two sets for skill comparison
my_skills = {"Python", "Git", "SQL"}
job_requirements = {"SQL", "Docker", "Linux", "Git"}

# 1. .add() — Add a single unique element
my_skills.add("Django")

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