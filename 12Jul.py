# l = [1,2,3,4,5,6,7,8,9,10,11]
# del l[3:5:2]     # l[start:end:step]
# print(l)

# Define the data
stdid = ["std101", "std102", "std103", "std104","std105", "std106", "std107", "std108", "std109", "std110"]
stdname = ["Ashish Kumar", "Abishek Kumar", "Aman", "Rahul", "Ruby", "Suman","Saurabh", "Sumit", "Kamlenh", "Rohan"]
standard = ["10th"]*10
Age =[15,14,15,14,13,13,15,14,15,15]
Hindi =[67,85,23,45,89,90,45,23,45,34]
English =[89,45,56,67,67,46,23,45,56,12]
Maths = [87,48,78,45,89,67,34,67,78,24]
Science = [89,90,78,45,93,67,45,78,99,45]
Computer = [90,45,67,56,67,34,90,67,56,50]
Total = [422,313,302,258,403,337,181,303,345,171]

data = [
    stdid,
    stdname,
    standard,
    Age,
    Hindi,
    English,
    Maths,
    Science,
    Computer,
    Total
]

headers = ["Student ID", "Student Name", "Standard", "Age", "Hindi", "English", "Maths", "Science", "Computer", "Total"]

transposed_data = list(zip(*data))

print(f"{' | '.join(headers)}")
for row in transposed_data:
    print(" | ".join(map(str, row)))




# Actions to name of student whose marks in English is >50
print("\nNames of students whose marks in English are greater than 50:")
for i in range(len(English)):
    if English[i] > 50:
        print(stdname[i]) 

    
# Actions to name and age of top four student in maths 
# Combine the relevant data into a list of tuples
students = list(zip(stdname, Age, Maths))

# Sort the students by their Maths scores in descending order
sorted_students = sorted(students, key=lambda x: x[2], reverse=True)

# Get the top four students
top_four_students = sorted_students[:4]

# Print the names and ages of the top four students in Maths
print("Name and age of the top four students in Maths:")
for student in top_four_students:
    print(f"Name: {student[0]}, Age: {student[1]}")
    
# display name ,id,age of student who are bottom three in Computer

students = list(zip(stdid,stdname, Age, Computer))

# Sort the students by their Maths scores in descending order
sorted_students = sorted(students, key=lambda x: x[3])

# Get the top four students
bottom_four_students = sorted_students[:4]

# Print the names and ages of the top four students in Maths
print("Name and age of the Bottom four students in Computer:")
for student in bottom_four_students:
    print(f"ID : {student[0]}, Name: {student[1]}, Age: {student[2]}")