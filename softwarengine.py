
def grade():
    i = 0
    sum = 0
    result_1 = 0
    num = int(input('Enter number of core courses offered this semester >>>'))
    for result_1  in range(num):
     course_code = str(input('Enter course codes here:'))
     course_unit = int(input('Enter course unit >>> '))
     grade = str(input('Enter your gotten grade of this course:'))
     if course_unit <= 10 and grade == 'A':
         result_1 = course_unit * 5
     elif course_unit <= 10 and grade == 'B':
         result_1 = course_unit * 4
     elif course_unit <= 10 and grade == 'C':
         result_1 = course_unit * 3
     elif course_unit <= 10 and grade == 'D':
         result_1 = course_unit * 2
     elif course_unit <= 10 and grade == 'E':
         result_1 = course_unit * 1
     else:
         result_1 = course_unit * 0
    sum+=result_1
    i+=1
    print(sum)
    