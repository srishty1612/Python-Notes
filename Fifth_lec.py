i=0
while i<=5:
    print(i)
    i+=1
print("Loop Ended")

# Print numbers from 1 to 100
i=1
while i<=100:
     print(i)
     i+=1

# print numbers from 100 to 1
i=100
while i>=1:
  print(i)
  i-=1

# print the multiplication table of a number n
n=int(input("Enter the number:"))
i=1
while i<=10:
    print(n*i)
    i+=1

#print the elements of the following list using a loop
[1,4,9,16,25,36,49,64,81,100]

# Break statement concept
i=0
while i<=5:
     print(i)
     if(i == 3):
         break
     i +=1

# Continue concept
i=0
while i<=5:
    if(i == 3):
        i += 1
    continue  #skip 
    print(i)
    i +=1

#for loop
movies=("kkk","dhishom","krish3","ishq")

for num in movies:
    print(num)

# Question for for loop
# print the elements of the following list using a loop
# [1,4,9,16,25,36,49,64,81,100]
list=[1,4,9,16,25,36,49,64,81,100]
for num in list:
    print(num)

# Search for a number x in this tuple using loop
# [1,4,9,16,25,36,49,64,81,100]
list=[1,4,9,16,25,36,49,64,81,100]
x=64
idx=0
for num in list:
     if(num==x):
          print("Found at index",idx)
     idx += 1
   
