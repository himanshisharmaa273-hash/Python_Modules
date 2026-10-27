'''MODULE-6 ASSIGNMENT'''
import csv
import json

'''Create And Write a File'''

with open("student.txt",'w') as file:
    file.write("Name: Himanshi Sharma")
    file.write("\nRoll Number:015")
    file.write("\nBranch:Computer Science and Engineering")
    file.write("\nCollege Name: BBDIT\n")
    
'''Read File Contents '''

with open('student.txt','r') as file:
    print(file.read())
    

'''Reading File contents Using ReadLine()'''

with open('student.txt','r') as file:
    print("="*30)
    print("READ FILE USING readline()")
    print("="*30)
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())
    
'''Reading File Contents using ReadLines()''' 

with open('student.txt','r') as file:
    
    print("="*30)
    print("READ FILE USING readlines()")
    print("="*30)
    print(file.readlines())
    

'''Append Existing File Student.txt '''

with open('student.txt','a') as file:
    sentence = input("\nEnter a sentence to append:-")
    file.write(sentence)
    
    
'''Count Lines, Words , and characters From a File'''

with open("student.txt",'r') as file:
    lines_count=0
    lines = file.readlines()
    
    for line in lines:
        lines_count+=1
    print("\nTotal number of lines in the file:",lines_count)
    
with open("student.txt",'r') as file:   
    words_count=0
    
    content = file.read()
    words = content.split()
    for word in words:
        words_count+=1
    print("\nTotal number of words in the file:", words_count)
    
with open('student.txt', 'r') as file:
    char_count=0
    content = file.read()
    
    for char in content:
        if char.isalpha():
            char_count+=1
    print("\nTotal number of characters in the file:", char_count)
    

'''Serach for a Word in File'''

with open("student.txt",'r') as file:
    
    content = file.read()
    search_word = input("\nEnter a word to search in file:")

    count = content.lower().count(search_word)
    
    print("\nTotal number of times, the word appear in file:",count)
    
    
'''Copy a content of a file and write it in another file'''

def copy_content(source, destination):
    with open(source,'r') as file:
        content = file.read()
    
    with open(destination,'w') as file:
        file.write(content)

def main():
    existing_file = 'student.txt'
    new_file ='data.txt'
    
    copy_content(existing_file, new_file)

main()


'''Read file line by line and displays line with its corresponding line number'''

with open('student.txt','r') as file:
    content = file.readlines()
    line_number =1
    
    for line in content:
        if line.strip()!=' ':
            print(line_number,line.strip())
            line_number+=1
            

'''Checking the Existence of a file'''

try:
    file_name = input("\nEnter a name of file Which you want to read:")
    with open(file_name,'r') as file:
        print(file.read())
    
except FileNotFoundError:
    print("File Not Found.Enter the name of existing file to read.")
    
    
'''Read and Write .CSV file'''

print("="*30)
print('\n OPERATIONS ON .CSV FILES')
print("="*30)

with open("students.csv",'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Roll_Number','Name','Marks'])
    
    for i in range(5):
        roll = int(input("Enter Roll Number of a student:"))
        name =input("Enter name of the student: ")
        mark=float(input("Enter marks of the student:"))
        print("\n")
        
        writer.writerow([roll,name,mark])
        
with open('students.csv','r') as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)


'''Filter CSV Records and read file using CSV.DictReader()'''

with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if float(row['Marks'])>=60:
            print(row)


print('='*30)
print('\nOPERATIONS ON .JSON FILE')
print('='*30)

'''OPERATIONS ON .JSON FILE'''

'''Using JSON.DUMP()'''

students =[{'Roll_No':101, 'Name':'Himanshi','Branch':'CSE','Marks':[98,97,99]},
           {'Roll_No':102, 'Name':'Khushi','Branch':'CSE','Marks':[96,97,95]},
           {'Roll_No':103, 'Name':'Prachi','Branch':'AI/ML','Marks':[89,92,90]},
           {'Roll_No':104, 'Name':'Elizabeth','Branch':'DS','Marks':[100,67,79]},
           {'Roll_No':105, 'Name':'Amrit','Branch':'AI/ML','Marks':[98,69,89]}]
with open("students.json",'w') as file:
    json.dump(students, file,indent=4)
    

'''USING JSON.LOAD()'''

with open('students.json','r') as file:
    students = json.load(file)
    # print(students)
    roll = int(input("Enter Roll number of the student:"))
    
    for student in students:
        if student['Roll_No']==roll:
            print(student)
        
        
    
'''ADD RECORD to .JSON'''  
 
new_student={'Roll_No':106,'Name':'Shradhha', "Branch":'VLSI','Marks':[78,87,92]} 
with  open('Students.json','r') as file:
    students=json.load(file)

    students.append(new_student)
            
        
with open('students.json','w') as file:
   json.dump(students,file,indent=4)
   

'''UPDATE  JSON Records'''

with  open('Students.json','r') as file:
    students=json.load(file)
    mark=list(map(int,input("Enter new marks of the student:").split()))
    roll = int(input("Enter roll number of the student whose details are to be updated:"))     
    for student in students:
        if student['Roll_No']==roll:
            student['Branch']= mark  

with open("students.json",'w') as file:
    json.dump(students, file, indent=4)
    
'''Delete JSON RECORD'''

with  open('Students.json','r') as file:
    students=json.load(file)
    roll = int(input("Enter roll number of the student to delete details:"))
    students=[student for student in students if student['Roll_No']!=roll]
    
with open("students.json",'w') as file:
    json.dump(students,file,indent=4)
            

    
'''JSON-to-CSV CONVERSION'''

students_detail=[{'roll_no':201,'name':'Sinchan','total_marks':98,'Avg_marks':66},
                 {'roll_no':202,'name':'Doraemon','total_marks':98,'Avg_marks':66},
                 {'roll_no':203,'name':'Spiderman','total_marks':98,'Avg_marks':66},
                 {'roll_no':204,'name':'Avtar','total_marks':98,'Avg_marks':66}
                 ]

'''Creating json file and write into it'''
with open("studentdata.json",'w+') as json_file:
    json.dump(students_detail,json_file,indent=4)
    
    
'''Reading the above created json file''' 
with open('studentdata.json','r') as json_file:
    data = json.load(json_file)
    # print(data)
    
'''Creating new CSV File'''
with open('Studentdata.csv','w',newline='') as csv_file:
    fields = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
    
print("JSON converted to CSV Successfully!")
    
    
    