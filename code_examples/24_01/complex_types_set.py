# Initialize two sets for skill comparison
# my_skills = {"Python", "Git", "SQL"}
# # job_requirements = {"SQL", "Docker", "Linux", "Git"}
# # 1. .add() — Add a single unique element
# print(my_skills)
# my_skills.add("Django")
# print(my_skills)
# my_skills.add("Django")
my_skills = {"Python", "Git", "SQL"}

my_skills = {"Python", "Git", "SQL"}
my_skills.add("Django")


my_skills["Python"]

# # # 2. .discard() — Safe removal (does not raise an error if item is missing)
# my_skills.discard("Java")
# random_value = my_skills.pop()
#
# color = {"Red", "Blue", "Green"}
#
# random_color = color.pop()
# color.add("Purple")
#
# color.update({"Yellow", "Grey"})
# # Always use list/set/tuple
# print(color)

# .clear() — Remove all elements from the set
# my_skills.clear()



# print(color)
# print(random_color)
#
# # 3. SET OPERATIONS (Mathematical logic):
#
# # Union (|) — Combine all unique elements from both sets
# all_skills = my_skills | job_requirements
#
# # Intersection (&) — Find elements present in both sets
# matching_skills = my_skills.intersection(job_requirements)
# print(f"I match the requirements for: {matching_skills}")
#
# # Difference (-) — Elements in the first set but not the second
# missing_skills = job_requirements - my_skills
# print(f"I need to learn: {missing_skills}")
#
# # 4. .clear() — Remove all elements from the set
# my_skills.clear()
#
#
# math example
first_plural = {1,2,3,4,5,6,7}
second_plural = {6,7,8,9,10}

union_plural = first_plural | second_plural
print(union_plural)
# #union_plural = first_plural.union(second_plural)
# print(union_plural)
#
intersection_plural = first_plural & second_plural
print(intersection_plural)
# #intersection_plural = first_plural.intersection(second_plural)
# print(intersection_plural)
#
difference_plural = first_plural - second_plural
# #difference_plural = first_plural.difference(second_plural)
print(difference_plural)


set_1 = [1,2,3,4,5,6,7,1,2,3,4,5,6,7]
var = set_1.sort() # sort does not return anything (NONE)
print(var) # var will be None
new_list = sorted(set_1) # sorted return a new object/ new list and original list is not changed
print(new_list)
print(set_1)