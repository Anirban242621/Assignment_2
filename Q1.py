#WAP to determine a student’s final grade and indicate whether they are passing or failing. The final grade is calculated as the average of marks of four subjects.
a = int(input('Enter marks of subject 1:'))
b = int(input('Enter marks of subject 2:'))
c = int(input('Enter marks of subject 3:'))
d = int(input('Enter marks of subject 4:'))
Grade = (a+b+c+d) / 4
print('Grade is : ',Grade)
if (Grade >= 40):
    print('Congratulation! You have Passed.')
else:
    print('Sorry, You failed.')