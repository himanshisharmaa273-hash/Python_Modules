
students = [
    {"roll_no": 101, "name": "himasnhi", "marks": 91},
    {"roll_no": 102, "name": "khushi", "marks": 88},
    {"roll_no": 103, "name": "Amrit", "marks": 94},
    {"roll_no": 104, "name": "jones", "marks": 76},
    {"roll_no": 105, "name": "Dr strange", "marks": 82},
    {"roll_no": 106, "name": "ironman", "marks": 90},
    {"roll_no": 107, "name": "spider man", "marks": 79},
    {"roll_no": 108, "name": "captain america", "marks": 95},
    {"roll_no": 109, "name": "batman", "marks": 84},
    {"roll_no": 110, "name": "wonder woman", "marks": 87},
]

print("\n=== Display All Students Roll-Name-Marks ===")
for student in students:
    print(student["roll_no"], student["name"], student["marks"])

print("\n==Highest Mark==")
highest_student = students[0]
for stud in students[1:]:
    if stud["marks"] > highest_student["marks"]:
        highest_student = stud

print(f"{highest_student['name']} - {highest_student['marks']}")

print("\n==Lowest Mark==")
lowest_student = students[0]
for stud in students[1:]:
    if stud["marks"] < lowest_student["marks"]:
        lowest_student = stud

print(f"{lowest_student['name']} - {lowest_student['marks']}")

print("\n==Average Marks==")
total_student = 10
total_marks = 0
for student in students:
    total_marks = total_marks+student["marks"]
   
Average_marks = total_marks/total_student
print("Average Marks :", Average_marks)

        

        
print("\n====Students Passed====")
passed = 0
fail = 0
for student in students:
    if student["marks"]>=40:
        passed = passed+1
    else:
        fail+=1
print("Passed:", passed)
print("failed:", fail)          


'''Sort students by marks'''
print("\n")
sorted_students = sorted(students, key=lambda student: student["marks"])
for student in sorted_students:
    print(student["name"], student["marks"])


'''Displaying Names in alphabetical order'''
students.sort(key= lambda student: student["name"])
print(students)

print("\n===========STUDENT REPORT===========")

print( "Total Students:",total_student)
print("Average Marks:", Average_marks)
print("\n")
print(f"Highest:\n {highest_student["name"]}-{highest_student["marks"]}")
print(f"Lowest:\n{lowest_student["name"]}-{lowest_student["marks"]}")
print("\nPassed:", passed)
print("\nFailed:", fail)

print("\n==Students Above 80==")
for student in students:
    if student["marks"]>80:
        print(student["name"])


print("\n Search student By Roll Number")
roll = int(input("Enter student Roll Number:"))
for student in students:
    if roll==student["roll_no"]:
        print(student)
