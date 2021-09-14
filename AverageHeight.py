
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

no_of_students=0
sum_of_heights=0

for i in student_heights[:]:
  no_of_students+=1

for i in student_heights[:]:
  sum_of_heights+=i


print(round(sum_of_heights/no_of_students))

# for student in student_heights:
#   no_of_students+=1

# for height in student_heights:
#   sum_of_heights+=height
