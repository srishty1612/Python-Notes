#Dictionary in Python

info = {
  "name":"Srishty",
 "age": 20,
  "Subjects": ["Java","Python","C++"],
  "Topics": ("Dictionary","Set")
 }
print(info)
print(type(info))
print(len(info))

info["name"]="Ram"
print(info)

null_dict={}
print(null_dict)

#Nested Dictionary
student = {
    "name":"Shyam",
    "age":18,
    "Subjects" :{
        "phy":80,
        "chem":95,
        "maths":90
    }
}
print(student)
print(student["Subjects"])
print(student["Subjects"]["maths"])

#Dictionary methods
print(list(student.keys()))
print(list(student.values()))
pairs=list(student.items())
print(pairs[2])
print(student.get("name"))
student.update({"location":"Delhi"})
print(student)


#set in python
sets={1,5,9,9,5,"Hello","Python","Hello"}  #we cannot store the dictionary and lists in sets because these are the mutable in nature but elements of sets are immutable in nature
print(sets)
print(type(sets))
print(len(sets))
empty_sets=set()  #syntax of empty set
print(empty_sets)
print(type(empty_sets))

#sets methods
collection={1,9,"Hello","coding","Learning"}
print(collection.add(5))
print(collection.remove(9))
print(collection.clear())
print(len(collection))
print(collection.pop())
set1={4,5,7}
set2={7,8,4,2}
print(set1.union(set2))
print(set1.intersection(set2))