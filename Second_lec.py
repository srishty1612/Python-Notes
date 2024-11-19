#String
str1="Srishty"
print(len(str1))
str2="Goyal"
print(len(str2))
last_str=str1+ " " + str2
print(last_str)
print(len(last_str))

#Indexing and Slicing
str= "Srishty Goyal"
print(str[4:9])
print(str[:4])
print(str[5:len(str)])
print(str[4:12])

#Slicing: Negative Indexing
string= "Mango"
print(string[-4:-1])

str="I am learning python"
print(str.endswith("on"))
print(str.capitalize())
str=str.capitalize()
print(str)
print(str.replace("python","C++"))
print(str.find("r"))
print(str.count("a"))


#If-elif-else condition
marks=85
if(marks>=80):
    print("Grade A+")  # these 4 spaces in python is known as indentation in place of {} brackets
elif(marks>=70 & marks<80):   #elif is check only when the if statement is false.it will not check when if statement is true
    print("Grade A")