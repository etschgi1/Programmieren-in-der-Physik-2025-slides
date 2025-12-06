student = {'name': 'Alice', 'age': 20, 'major': 'Computer Science', 'GPA': 3.8}
# Change the value of a key
student['name'] = 'Bob'
# Add a new key-value pair
student["courses"] = ['Math', 'CompSci']
# Deletes "age" - key-value pair
del student['age']
all_keys = student.keys()
all_values = student.values()
all_items = student.items()
for key in student.keys():
    print(key)
