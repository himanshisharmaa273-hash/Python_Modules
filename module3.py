'''LEVEL 1 == String'''

name = "Himanshi Sharma"
print(len(name))

print(f"first character:{name[0]},\n last character:{name[-1]}")

print(f"Reversed String:{name[::-1]}")

count = 0
spaces =0
vowels=('a','i','e','o','u')
for ch in name:
     if ch.lower() in vowels:
         count+=1
     elif ch.isspace():
         spaces+=1
print("Total vowels in the string:", count)

print("Total Spaces in the string:", spaces)

print(name.upper())

if   name[0:2]=="Py": #name.startswith("Py")
    print("string is starting with 'Py'.")
else:
    print("String is not started with 'Py'.")
    
new_name = name.replace(" ","-")
print(new_name)

char = input("Enter a particular charcter: ")
char_count = 0
#char_count = name.count(ch):
for ch in name.lower():
     if char.lower()==ch:
         char_count+=1
print(f"occurence of character {char} in the string:{char_count}")

if name==name[::-1]:
     print("String is palindrome.")
else:
     print("String is not palindrome.")
    


'''LEVEl 2 ==Lists'''
list1 = list(map(int,input("Enter the elements of the list(Separated by commas):").split(",")))
print("Your list is ", list1)
print("The largest number  in the list is ", max(list1))

print("\n The smallest number in the list is", min(list1))

Sum_list = sum(list1)
length = len(list1)
average = Sum_list/length
print(f"\n Sum of the list is {Sum_list} and Average is {average}")

count = 0
for num in list1:
     if num%2==0:
         count+=1
print("\n Total even number exist in the list is", count)

new_list = list(set(list1))
print("List after removing duplicates:", new_list)


list1.sort()
sec_highest = list1[-2]
print("\n Second Highest number in the list is", sec_highest)
l1 =[2,3,4,5,6]
print(sorted(set(l1))[-2])

reversed_list = list1[::-1]
print("\n Reversed list:", reversed_list)

l1 = [1,2,3,45,32,23,5,6]
l2 = [978,5,75,85,2,6,2]
l3 = [i for i in l1 if i in l2]
print("\n common elements between two list are:",l3)

print("\n merged list:", l1+l2)


even_list= [ i for i in list1 if i%2==0]
odd_list = [i for i in list1 if i%2!=0]
print(f"\n Even number list is {even_list}\n Odd number list is {odd_list}")



'''LEVEL - 03===Dictionary'''
student = {'name':'Himanshi', 'age':20, 'course':'B.tech', 'branch':'CSE'}
print("Student Details:", student)

student['state']= 'Uttar Pradesh'
student['age']= 19
print("\n Updated student details:", student)

string = input("Enter a string:")
frequency = {}
for ch in string:
     if ch in frequency:
         frequency[ch]+=1
     else:
         frequency[ch]=1
print("\n Frequency of each character:", frequency)

sentence =input("Enter a sentence:")
frequency={}
for word in sentence.split():
     if word in frequency:
         frequency[word]+=1
     else:
         frequency[word]=1
print("\n frequency of words in sentence:", frequency)



'''LEVEL 04===Mixed questions'''

string1 = input("Enter the 1st string:")
string2 = input("Enter the 2nd String:")
if len(string1)!=len(string2):
     print("Not valid anagrams.")
else:
     for i in string1:
         if i in string2:
             print("Valid Anagrams.")
             break
            

list2 = [1,2,3,4,5,2,3,4,5,6,4,2,6,7,8,5,2,7]
dulpicates=[]
for num in list2:
    if list2.count(num)>1:
         dulpicates.append(num)
print("\n list of duplictes number:", set(dulpicates))

l1= list(map(int, input("Enter the numbers of 1st list:").split(" ")))
l2= list(map(int, input("Enter the numbers of 2nd list:").split(" ")))
l3= list(map(int, input("Enter the numbers of 3rd list:").split(" ")))

common_elements=[i for i in l1 if i in l2 and i in l3]
print("\n common elements among three lists:", common_elements)


list3 = [1,2,3,4,2,3,1,4,5,6,4,7,4,7,4,25,5]       
most_frequent = max(list3, key=list3.count)
print("\n Most frequent number in the list is ", most_frequent)

string1 = input("Enter a sentence:")
words = string1.split()
unique_words = []

for word in words:
     if word not in unique_words:
         unique_words.append(word)

print(" ".join(unique_words))
        
    