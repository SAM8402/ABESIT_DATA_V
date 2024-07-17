# Initial list and deletion operation
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
del l[3:5]  # Correcting the deletion slice
print(l)

# Define the data
stdid = ["std101", "std102", "std103", "std104", "std105", "std106", "std107", "std108", "std109", "std110"]
stdname = ["Ashish Kumar", "Abishek Kumar", "Aman", "Rahul", "Ruby", "Suman", "Saurabh", "Sumit", "Kamlenh", "Rohan"]
standard = ["10th"] * 10
Age = [15, 14, 15, 14, 13, 13, 15, 14, 15, 15]
Hindi = [67, 85, 23, 45, 89, 90, 45, 23, 45, 34]
English = [89, 45, 56, 67, 67, 46, 23, 45, 56, 12]
Maths = [87, 48, 78, 45, 89, 67, 34, 67, 78, 24]
Science = [89, 90, 78, 45, 93, 67, 45, 78, 99, 45]
Computer = [90, 45, 67, 56, 67, 34, 90, 67, 56, 50]
Total = [422, 313, 302, 258, 403, 337, 181, 303, 345, 171]

data = {
    "stdid": stdid,
    "stdname": stdname,
    "standard": standard,
    "Age": Age,
    "Hindi": Hindi,
    "English": English,
    "Maths": Maths,
    "Science": Science,
    "Computer": Computer,
    "Total": Total
}

headers = ["Student ID", "Student Name", "Standard", "Age", "Hindi", "English", "Maths", "Science", "Computer", "Total"]

# Print the headers and data
print(f"{' | '.join(headers)}")
for i in range(len(data["stdid"])):
    row = [data[key][i] for key in data]
    print(" | ".join(map(str, row)))

# Print names of students whose marks in English are greater than 50
print("\nNames of students whose marks in English are greater than 50:")
for i in range(len(data["English"])):
    if data["English"][i] > 50:
        print(data["stdname"][i])

# Combine the relevant data into a list of dictionaries for Maths
students_math = [{"name": data["stdname"][i], "age": data["Age"][i], "maths": data["Maths"][i]} for i in range(len(data["stdid"]))]

# Sort the students by their Maths scores in descending order
sorted_students_math = sorted(students_math, key=lambda x: x["maths"], reverse=True)

# Get the top four students in Maths
top_four_students_math = sorted_students_math[:4]

# Print the names and ages of the top four students in Maths
print("\nName and age of the top four students in Maths:")
for student in top_four_students_math:
    print(f"Name: {student['name']}, Age: {student['age']}")

# Combine the relevant data into a list of dictionaries for Computer
students_computer = [{"id": data["stdid"][i], "name": data["stdname"][i], "age": data["Age"][i], "computer": data["Computer"][i]} for i in range(len(data["stdid"]))]

# Sort the students by their Computer scores in ascending order
sorted_students_computer = sorted(students_computer, key=lambda x: x["computer"])

# Get the bottom three students in Computer
bottom_three_students_computer = sorted_students_computer[:3]

# Print the ID, name, and age of the bottom three students in Computer
print("\nID, name, and age of the bottom three students in Computer:")
for student in bottom_three_students_computer:
    print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
