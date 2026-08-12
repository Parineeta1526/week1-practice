courses={
    "Python":25,
    "Java":18,
    "SQL":30,
    "Web":15
}
print("Course Enrollments:")
for course,students in courses.items():
    print(f"{course}:{students}")
name=input("Enter course name:")
if name in courses:
    print(f"Course enrollment in {name}:{courses[name]}")
else:
    print("Course not found")
total=sum(courses.values())
highest=max(courses.values())
lowest=min(courses.values())
print(f"Total enrollments: {total}")
print(f"Highest enrollment: {highest}")
print(f"Lowest enrollment: {lowest}")