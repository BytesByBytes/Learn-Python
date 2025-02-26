last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]


gradebook = [["physics", 98],["Calculus", 97],["poetry", 85],["history", 88]]

gradebook.append(["computer_science", 100])

#Visual Arts Chages 
gradebook.append(["visual_arts", 93])
gradebook[-1][-1] = 93 + 5

gradebook[2].remove(85)
gradebook[2].append("Pass")

full_gradebook = (last_semester_gradebook + gradebook)
print(full_gradebook)