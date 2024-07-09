# Write a python program to create a list with all the subject names of the 4th 
# semester and perform the following operations. 
# • Display the list using for loop. 
# • Display 2nd and 5th element of the list. 
# • Display first 4 elements of the list using the range of indexes. 
# • Display last 4 elements of the list using the range of negative indexes. 
# • Display if "Python Programming Lab" is available in the List or not. 
# • Demonstrate the working of append () and insert () function. 
# • Demonstrate the working of remove() and pop() function. 

subjects = ["Data Structures", "Computer Networks", "Operating Systems", "Python Programming Lab", "Java Programming Lab", "Computer Networks Lab", "Operating Systems Lab"]

print("List of subjects in 4th semester:")
for subject in subjects:
    print(subject)
print()

print("2nd and 5th element of the list:")
print(subjects[1], subjects[4])
print()

print("First 4 elements of the list:")
print(subjects[:4])
print()

print("Last 4 elements of the list:")
print(subjects[-4:])
print()

if "Python Programming Lab" in subjects:
    print("Python Programming Lab is available in the list")
print()

subjects.append("Data Mining")
print("After appending Data Mining:")
print(subjects)
print()

subjects.insert(2, "Machine Learning")
print("After inserting Machine Learning at index 2:")
print(subjects)
print()

subjects.remove("Data Mining")
print("After removing Data Mining:")
print(subjects)
print()

subjects.pop(2)
print("After popping element at index 2:")
print(subjects)
print()
