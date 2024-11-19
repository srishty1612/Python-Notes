marks=[69.5,45.7,85.12,98.2]
print(marks)
print(type(marks))
print(len(marks))
print(marks[2])
print(marks[3])

student=["Ram",98,22,"Jaipur"]
print(student)
student[2]=20 #we can change the value of a index in list as it is a mutable in nature
print(student)

#As in string,list also has slicing which is same as string slicing

#List Methods

number=[89,45,12,45]
number.append(6)  #adds one element at the end
print(number)
number.append("Ram")
print(number)

number.sort()
print(number.sort())
print(number)
number.sort(reverse=True)
print(number)
number.reverse()
print(number)

number.insert(2,6)
print(number)
number.remove(45)
print(number)
number.pop(3) #remove at index ind
print(number)


#TUPLES IN PYTHON
tupel=(45,23,62)
print(tupel)
print(len(tupel))
print(type(tupel))
print(tupel[2])

tup=()  #tuple with null values
print(tup)
print(type(tup))

tupe=(1,)  #if we have to save a single value in a tuple then we have to separate with a comma but not compulsory in multiple values
print(tupe)
print(type(tupe))

#Slicing in tuples is same as in string and lists

#tuple methods
tuple=(3,8,7,5)
print(tuple.index(7))  #here 7 is element which is to be searched
print(tuple.count(8))



