student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇

for x,y in student_scores.items():
    if y>=90:
        student_grades[x]="Outstanding"
    elif y>81:
        student_grades[x]="Exceeds Expectations"
    elif y>71:
        student_grades[x]="Acceptable"
    else:
        student_grades[x]="Fail"
  


print(student_grades)





