print(" Welcome to the Marks Percentage Calculator!\n")

sub1 =int(input("enter the marks of first subject: "))
sub2 =int(input("enter the marks of second subject: "))
sub3 =int(input("enter the marks of third subject: "))
sub4 =int(input("enter the marks of fourth subject: "))
sub5 =int(input("enter the marks of fifth subject: "))

total_marks = 500
obtain_marks = sub1+sub2+sub3+sub4+sub5

percentage = (obtain_marks/total_marks)*100

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
else:
    grade = "Fail"

print("------------RESULT------------")
print(f"Total Marks are {total_marks}")
print(f"obtain_marks are {obtain_marks}")
print(percentage)
print(grade)