# [I] LISTS

courses=['History', 'Math', 'Phy', 'CompSci']
print(courses)
print(len(courses)) # 4

#Slicing
print(courses[1:3]) # ['Math', 'Phy']
print(courses[2]) # Phy
print(courses[-1]) # CompSci

# Append method
courses.append('Art')
print(courses) # ['History', 'Math', 'Phy', 'CompSci', 'Art']

# Insert method (index, value)
courses.insert(2, 'Music')
print(courses) # ['History', 'Math', 'Music', 'Phy', 'CompSci', 'Art']

# Extend method
courses_2=['Civics', 'Games']
courses.extend(courses_2)
print(courses) # ['History', 'Math', 'Music', 'Phy', 'CompSci', 'Art', 'Civics', 'Games']

# Remove method
courses.remove('Math')
print(courses)

# Pop Method: pops the last element
popped = courses.pop() # popped value is Games
print('popped value is ' + popped)
print(courses) # ['History', 'Music', 'Phy', 'CompSci', 'Art', 'Civics']

# Reverse Method
courses.reverse()
print(courses) # ['Civics', 'Art', 'CompSci', 'Phy', 'Music', 'History']

# Sort method: sorts in alphabeticaal order
courses.sort()
print(courses) # ['Art', 'Civics', 'CompSci', 'History', 'Music', 'Phy']
courses.sort(reverse=True)
print(courses) # ['Phy', 'Music', 'History', 'CompSci', 'Civics', 'Art']

# Sorted method
sorted_courses = sorted(courses)
print(sorted_courses) # ['Art', 'Civics', 'CompSci', 'History', 'Music', 'Phy']

# Min Max Sum
nums=[1,5,3,4,2]
print(min(nums)) # 1
print(max(nums)) # 5
print(sum(nums)) # 15

# Index method
print(nums.index(3)) # 2

# In Method
print('Music' in courses) # True

# For Loop
for i in courses:
    print(i)
# Phy
# Music
# History
# CompSci
# Civics
# Art

for index, course in enumerate(courses):
    print(index, course)
# 0 Phy
# 1 Music
# 2 History
# 3 CompSci
# 4 Civics
# 5 Art

for index, course in enumerate(courses, start=1):
    print(index, course)
# 1 Phy
# 2 Music
# 3 History
# 4 CompSci
# 5 Civics
# 6 Art

# Join Method: List to String
course_str = ' - '.join(courses)
print(course_str) # Phy - Music - History - CompSci - Civics - Art

# Split Method: String to list
new_list = course_str.split(' - ')
print(new_list) # ['Phy', 'Music', 'History', 'CompSci', 'Civics', 'Art']

# [II] TUPLES

tuple_1 = ('History', 'Math', 'Phy', 'CompSci')
tuple_2 = tuple_1

print(tuple_1) # ('History', 'Math', 'Phy', 'CompSci')
print(tuple_2) # ('History', 'Math', 'Phy', 'CompSci')

# tuple_1[0]='Art' # TypeError: 'tuple' object does not support item assignment

# [III] SETS
cs_courses = {'History', 'Math', 'CompSci', 'Physics', 'Math'}
print(cs_courses) # {'Physics', 'Math', 'History', 'CompSci'}
# Note: the print order changes with each execution; Sets dont care about order
# Note: Sets remove duplicates, thus Math returned only once
print('Math' in cs_courses) # True

# Intersection and Difference Method
art_courses={'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses)) # {'Math', 'History'}
print(cs_courses.difference(art_courses)) # {'CompSci', 'Physics'}

# Union Method
print(cs_courses.union(art_courses)) # {'Math', 'Physics', 'Design', 'CompSci', 'Art', 'History'}



# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}  # This isn't right! It's a dict.
empty_set = set()






