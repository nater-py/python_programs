# Gradebook Project

# You are a student and you are trying to organize your subjects and grades using Python. Organize your subjects and scores using your knowledge of lists. 

# Last Semester Gradebook

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Lists for Subjects and Grades

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

# Creating 2D List to combine Subjects & Grades

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Adding Computer Science Subject & Grade to Gradebook using 'append' Method

gradebook.append(["computer science", 100])

# Adding Visual Arts Subject & Grade to Gradebook using 'append' Method

gradebook.append(["visual arts", 93])

# Updating Visual Arts grade to '98' from '93' by accesing indices

gradebook[-1][1] = 98

# Switching Numerical Grade value to Pass/Fail for Poetry Class

gradebook[2].remove(85)
gradebook[2].append("Pass")

# Printing the contents of the gradebook
print(gradebook)

# Combining grades from last semester & this semester into one big gradebook

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
