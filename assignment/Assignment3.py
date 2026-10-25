'''MODULE -4 ASSIGNMENT'''

'''==============================
    STUDENT PERFORMANCE SYSTEM
==============================='''

Students_list=[]

subjects = ['Python','DBMS', 'OS', 'Maths', 'CN']

'''ADD  STUDENTS '''
def add_student():
    
    
    name = input("Enter Student name:")
    roll = int(input("Enter Roll Number:"))
    marks =[]
    
    for subject in subjects:
        while True:
            mark = float(input(f"Enter Marks in {subject}:"))
            if 0<=mark<=100:
                marks.append(mark)
                break
            else:
                print("Marks must be in between 0-100")
               
    students={"Name":name, "Roll":roll, "Marks":marks}
    Students_list.append(students)
         
    print("\n!!Student Added Successfully!!")
    
    
'''DISPLAY STUDENTS'''
def display_student():
    if len(Students_list)==0:
        print("\nEmpty student details ")
        return
    
    print("\n"+'='*70)
    print(f"{'Name':<20}{'Roll_Number':<20}{'Total_Marks':<20}{'Percentage(%)':<15}{'Grade':<5}")
    print("\n"+'='*70)
    
    for student in Students_list:
        total_marks = calculate_total_Marks(student)
        percentage=calcuate_percentage(student)
        grade = calculate_grade(student)
        
        print(f"{student['Name']:<20}"f"{student['Roll']:<20}"f"{total_marks:<20}"f"{percentage:<15}"f"{grade:<5}")


'''SEARCH STUDENTS'''
def search_student():
    if len(Students_list)==0:
        print("No Record is Available!")
        return
    
    roll = int(input("Enter Roll Number of the student:"))
    for student in Students_list:
        if student['Roll']==roll:
            student_result(student)
            return
    
    print("\n Student details are not found")
 
            
            
''' INDIVIDUAL STUDENT RESULT '''       
def student_result(student):
    
    if len(Students_list)==0:
        print("\n No records!!")
        return
    
    print(f"Name:{student['Name']}")
    print(f"\n Roll Number:{student['Roll']}")
    print("\n Marks:")
     
    for i in range(5):
        print(f"{subjects[i]}:{student['Marks'][i]}")
        
    print(f"\nTotal:{calculate_total_Marks(student)}")
    print(f"\nPercentage:{calcuate_percentage(student)}")
    print(f"{calculate_grade(student)}")



'''TOTAL MARKS CALCULATION'''
def calculate_total_Marks(student):
    return sum(student['Marks'])


'''PERCENTAGE CALCULATION'''
def calcuate_percentage(student):
    Total_marks = calculate_total_Marks(student)
    percentage = Total_marks/5
    
    return percentage


'''GRADE CALCULATION'''
def calculate_grade(student):
    percentage = calcuate_percentage(student)
    
    if percentage>=90:
        return ('Grade: A')
    elif percentage>=80:
        return ("Grade: B")
    elif percentage>70:
        return ("Grade: C")
    elif percentage>60:
        return ("Grade: D")
    else:
        return ("Fail")


'''FIND TOPPER'''

def find_topper():
    if len(Students_list)==0:
        print("Empty Records")
        return
    
    topper = Students_list[0]
    
    for student in Students_list:
        if calcuate_percentage(student)>calcuate_percentage(topper):
            topper = student
    
    print("TOPPER DETAILS")
    print(f"Name:{topper['Name']}")
    print(f"Name:{topper['Roll']}")
    print(f"Name:{calcuate_percentage(topper)}")
    print(f"Name:{calculate_grade(topper)}")



''' CLASS STATISTICS''' 
def display_statistics():
    if len(Students_list)==0:
        print("NO record found!!")
        return
    
    percentages =[]
    percentages =[calculate_total_Marks(student) for student in Students_list]
    # for student in Students_list:
    #     percentages.append(calculate_total_Marks(student))
       
    total_students=len(Students_list)
    class_Average=sum(percentages)/total_students
    highest_percentage=max(percentages)
    lowest_percentage=min(percentages)
    topper = percentages.index(highest_percentage)
    
    Passed = [percentage for percentage in percentages if percentage>=60]
    failed = [percentage for percentage in percentages if percentage<60]
    
    print("CLASS STATISTICS")
    print(f"\n Total Students:{total_students}")
    print(f"\n Class Average:{class_Average}")
    print(f"\n Highest Percentage:{highest_percentage}")
    print(f"\n Lowest Percentage:{lowest_percentage}")   
    print(f"\n Topper:{Students_list[topper]['Name']}") 
    print(f"Number of Students Passed:{len(Passed)}")
    print(f"Number of Students Failed:{len(failed)}")



'''STUDENT SORTING BASED ON PERCENTAGE'''
def sort_students():
    if len(Students_list)==0:
        print("\n No records!!")
        return
    
    sorted_students=sorted(Students_list, key=calcuate_percentage, reverse=True)
        
    for student in sorted_students:
        percentage = calcuate_percentage(student)
            
        print(f"{student['Name']:<20}"f"Roll:{student["Roll"]:<10}"f"Percentage:{percentage:2f}%")
      
    

'''DELETE STUDENT'''  
def delete_student():
    if len(Students_list)==0:
        print("\n No Records !!")
        return
    
    roll = int(input("Enter Roll number of student to delete:"))
    
    for student in Students_list:
        if student['Roll']==roll:
            Students_list.remove(student)
            print("\nStudent Deleted Successfully!!")
            return
    print('\nStudent Not Found')
    

'''UPDATE STUDENTS MARKS'''
def update_marks():
    if len(Students_list)==0:
        print("\n No records!!")
        return

    roll = int(input("Enter roll Number of student:"))
    
    for student in Students_list:
        if student['Roll']==roll:
            
            print("\n Enter new marks:")
            for i in range(5):
                
                while True:
                    
                    mark = float(input(f"Enter New Marks for {subjects[i]}:"))
                    if 0<=mark<=100:
                        student['Marks'][i]=mark
                        break
                    else:
                        print("Marks must be in between 0-100")
            
            print("\nMarks Updated Successfully")
            return
        
    print("\nStudent Not Found")              
  
'''STUDENTS ABOVE 80%'''  
def students_above_80():
    if len(Students_list) == 0:
        print("\nNo student records available.")
        return

    found = False

    print("\n====== STUDENTS ABOVE 80% ======")

    for student in Students_list:

        percentage = calcuate_percentage(student)

        if percentage > 80:
            found = True

            print(f"Name: {student['Name']:<20}"f"Roll: {student['Roll']:<10}"f"Percentage: {percentage:.2f}%"
)

    if not found:
        print("No student scored above 80%.")

while True:

    print("\n")
    print("=" * 40)
    print("     STUDENT PERFORMANCE SYSTEM")
    print("=" * 40)   

    print('1.Add Student')
    print('2.Display Students')
    print('3.Search Student')
    print('4.Student Result')
    print('5.Find Topper')
    print('6.Class Statistics')
    print('7.Sort Students By Percentage')
    print('8.Delete Student')
    print('9.Update Student Marks')
    print('10.Show Students Who Scored >80%')
    print('11.Exit')
    
    choice = int(input("\nEnter your Choice:"))  
    
    if choice==1:
        add_student()
    
    elif choice==2:
        display_student()
        
    elif choice==3:
        search_student()
        
    elif choice==4:
        roll = int(input("Enter roll Number:"))
        
        for student in Students_list:
            if student["Roll"]==roll:
                student_result(student)
                
    elif choice==5:
        find_topper()
    
    elif choice==6:
        display_statistics()
        
    elif choice==7:
        sort_students()
    
    elif choice==8:
        delete_student()
    elif choice==9:
        update_marks()
    elif choice==10:
        students_above_80()
    elif choice==11:
        print("\n Exiting....")
        break
    
    else:
        print("\n Invalid Choice.Please Try Again")
                  