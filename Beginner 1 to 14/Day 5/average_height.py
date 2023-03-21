# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
num_heights = 0
total = 0

for height in student_heights:
    num_heights += 1
    total += height

print(round(total / num_heights))


