# >>>>>>>>>Question 1 :- String operations with name.........

name = "Rahul"

print(name[0])         
print(name[-1])         
print(len(name))        
print(name.upper())     
print(name.lower())    
print(name[::-1])       


# >>>>>>>>Question 2 :- String slicing.............

text = "Hacker"

print(text[0:4])        
print(text[2:6])       
print(text[::-1])       


# Question 3 - List operations

num = [10, 20, 30, 40, 50, ]

num.append(60)
print(num)

num.insert(2, 99)
print(num)

num.remove(99)
print(num)

num.pop()
print(num)

num.reverse()
print(num)

num.sort()
print(num)

print(len(num))

print(num.count(10))



# >>>>>>>>>>>>>Question 4 :- Tuple operations..........

subjects = ("Math", "Science", "English", "Hindi", "Computer")

print(subjects[0])
print(subjects[-1])
print(len(subjects))
print(subjects[1:4])

nums = (10, 50, 30, 20, 40)
print(max(nums))
print(min(nums))
print(sum(nums))



# >>>>>>>>>>>>>Question 5 :- Tuple packing and unpacking..........

my_tuple = ("Rahul", 20, "CSE", "Jaipur")

name, age, course, city = my_tuple

print(name)
print(age)
print(course)
print(city)


# >>>>>>>>>>>>>>>Question 6 :- Dictionary - student details......

student = {
    "Name": "Rahul",
    "Age": 20,
    "Course": "B.Tech CSE",
    "Address": "Jaipur"
}

print(student.keys())
print(student.values())
print(student.items())

student["Address"] = "Jodhpur"
print(student)

student["Branch"] = "AI & ML"
print(student)


# >>>>>>>>>>>>Question 7 :- Nested list element access....

my_list = [1, 2, 3, 4, [2, 5], 7]

print(my_list[4][1])    



# >>>>>>>>Question 8 - += operator.........

num = int(input("Enter a number: "))

num += 10

print(num)



# >>>>>>>>>>>Question 9 - Type casting..........

a = input("Enter first number: ")
b = input("Enter second number: ")

a = int(a)
b = int(b)

print(a * b)



#>>>>>>>>>>> Question 10 :- Dictionary methods.........

info = {
    "name": "Rahul",
    "age": 20,
    "city": "Jaipur"
}

print(info.get("name"))
print(info.get("phone", "Not found"))  

print(info.keys())
print(info.values())
print(info.items())


#>>>>>>>> Question 11 :- List copy..............

original = [1, 2, 3, 4, 5]

copied = original.copy()

print(original)
print(copied)