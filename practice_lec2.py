#Question 1
#WAP to input users first name and print its length
#Answer is
name=input("enter your name:")
print(len(name))

#Question 2
#Wap to fing the occurence of $ in a string
str="College$"
print(str.count("$"))

marks=float(input("Enter the marks of student:"))
if(marks>=90):
    Grade="A"
elif(marks<90 and marks>=80):
    Grade="B"
elif(marks<80 and marks>=70):
    Grade="C"
elif(marks<70):
    Grade="D"
print("Grade of the student",Grade)

#Question 3
#WAP to check if a number entered by the user is odd or even
#Answer is
num=int(input("Enter the number:"))
if(num%2==0):
    print("Number is even")
else:
    print("Number is odd")

#Question 4
#WAP to find the greatest of 3 numbers enterd by the user
#Answer is
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the thired number:"))
if(num1>num2 and num1>num3):
    print("Num1 is greater than other two numbers")
elif(num2>num3 and num2>num1):
    print("Num2 is greater than other two numbers")
else:
    print("Num3 is greater than other two numbers")


#Question 5
#WAP to check if a number is a multiple of 7 or not
#Answer is
a=int(input("Enter the number:"))
if(a%7==0):
    print("number is multiple of 7")
else:
   print("number is not multiple of 7")