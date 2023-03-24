# This is Day 5 of 100 for the Udemy Python Bootcamp

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

#total of height entries
total_height = 0
for height in student_heights:
    total_height += height
print("Total heights add up to: ", total_height)

#number of entries
num_heights = 0
for entry in student_heights:
    num_heights += 1
print("Number of entry values is: ",num_heights)

#average = total of heights / number of values
average_height = total_height / num_heights

#round and print
print("The average height is: ", round(average_height))