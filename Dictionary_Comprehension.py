# Dictionary Comprehension
# {new_key:new_value for key,value in dict.items()}

# Generate a dictionary of random students scores from given list of students.
import random
students = ["Beth", "Carolina", "Daisy", "Piyush", "Jyoti"]
students_marks = {student:random.randint(1,100) for student in students}
print(students_marks)

# How to use Condition in Dictionary 
# generate the dictionary of passed students from above dictionary.
passed_students = {student:score for student,score in students_marks.items() if score > 40}
print(passed_students)

# Print length of each word in given sentence.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

# Convert dictionary having temperatures in Celsius to Fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f={day:(temp*9/5 + 32) for day,temp in weather_c.items()}
print(weather_f)

# Looping through Pandas dataframe
import pandas
student_dict={
    "students":["Beth", "Carolina", "Daisy", "Piyush", "Jyoti"],
    "scores":[45,56,78,25,98]
    }
student_data_frame = pandas.DataFrame(student_dict)

for (index,row) in student_data_frame.iterrows():
    # print(row)
    # print(index)
    print(row["students"])