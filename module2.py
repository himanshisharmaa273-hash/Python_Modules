age = int(input("Enter your age:"))
if age>=18:
    print("person is eligible to vote!")
else:
    print("Person is not eligible to vote!!")


num1 = float(input("Enter 1st num:"))
num2 = float(input("Enter 2nd num:"))

if num1==num2:
    print("both numbers are equal.")
elif num1>num2:
    print(f"{num1} is greater than{num2}.")
else:
    print(f"{num2} is greater than {num1}.")



year = int(input("Enter a year:"))

if (year%400==0) or ((year%4==0) and (year%100!=0)):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year")

char = input("Enter any alphabet:")
if char.lower() in "aeiou":
    print("entered alphabet is vowel.")
else:
   print("entered character is consonant")

purchase_amount = float(input("Enter purchase amount:"))
if purchase_amount>=2000:
    discount = 0.2 * purchase_amount
    print(f"your discount amount is {discount}")
else:
    print("No discount for purchase amount less than 2000.")


# num = int(input("Enter any number within range of 20 and 50:"))

# if 20<=num<=50:
#     print("Entered number lies within range of 20 and 50.")
# else:
#     print("number is not in range of 20 and 50")

# for i in range(1,101):
#     print(i)   

# for i in range(100, 0,-1):
#     print(i)

# for i in range(1,101):
#     if i%2==0:
#         print(i)

# for i in range(1,101):
#     if i%2!=0:
#         print(i)

# num = int(input("Enter a number which table you want:"))
# print(f"table for {num}:-")
# for i in range(1,11):
#     print(f"{num}x{i}={num*i}")

# n = int(input("Enter value of n:"))
# sum = 0 
# for i in range(1,n+1):
#     sum+=i
# print("sum of numbers from 1 to n is", sum)   
    
# n = int(input("enter value of n:"))
# sum = 0
# for i in range(1,n+1):
#     if i%2==0:
#         sum+=i
# print("sum of even numbers from 1 to n is", sum)

# count = 0
# for i in range(1,100):
#     if i%3==0:
#         count+=1
# print(" total numbers divisible by 3 between 1 and 100 are", count)

# num = 12
# while True:
#     guess = int(input("Enter guess number:"))
#     if num!=guess:
#         print("You guessed wrong number. Enter other number:")
#     else:
#         print("Right guess")

'''WRONG OUTPUT IN FEW  CASES'''

# num = 12
# gues_num = int(input("Enter a number to guess:"))
# while  num!=gues_num:
#     print("wrong guess!! Try Again")
#     break
# if num ==gues_num:
#     print("Correct Guess.")
    