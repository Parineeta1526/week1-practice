name=input("Enter student name:")
sub1=int(input("Enter marks of subject 1:"))
sub2=int(input("Enter marks of subject 2:"))
sub3=int(input("Enter marks of subject 3:"))
sub4=int(input("Enter marks of subject 4:"))
sub5=int(input("Enter marks of subject 5:"))
marks=[sub1,sub2,sub3,sub4,sub5]
total=sub1+sub2+sub3+sub4+sub5
average=total/5
highest=max(marks)
lowest=min(marks)
passed=0
failed=0
for mark in marks:
    if mark>=40:
        passed=passed+1
    else:
        failed=failed+1
if average>=90:
    grade='A'
elif average>=75:
    grade='B'
elif average>=60:
    grade='C'
elif grade>=40:
    grade='D'
else:
    grade='F'
print(f"Student name: {name}")
print(f"Total marks: {total}")
print(f"Average marks: {average}")
print(f"Highest marks: {highest}")
print(f"Lowest marks: {lowest}")
print(f"Number of subjects passed: {passed}")
print(f"Number of subjects failed: {failed}")
print(f"Grade: {grade}")