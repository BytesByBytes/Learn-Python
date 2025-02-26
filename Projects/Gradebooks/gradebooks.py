last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#Create lists for subjects and grades

subject = ["physics", "calculus", "poetry", "history"]
grade = [98, 97, 85, 88]


gradebook = [["physics", 98],["calculus", 97],["poetry", 85],["history", 88]]

# Remove the grade and append "Pass" for the poetry subject
gradebook.remove(["poetry", 85])
gradebook.append(["poetry", "Pass"])

# Appending data in a way to improve performance
for subject, grade in [("computer_science", 100), ("visual_arts", 93)]:
    gradebook.append([subject, grade])
    
if len(gradebook) > 0 and len(gradebook[-1]) > 1:
    gradebook[-1][-1] = 98


full_gradebook = (last_semester_gradebook + gradebook)
print(full_gradebook)