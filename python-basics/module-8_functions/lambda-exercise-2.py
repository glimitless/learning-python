students = [
    ['Blue', 99],
    ['Yuusef', 51],
    ['Gian-I', 84],
    ['Max', 63]
]


pass_criteria = lambda mark: mark > 70
passed_course = lambda student: pass_criteria(student[1])
passing_students = filter(passed_course, students)

print('All students:', students)
print('Students that passed:', list(passing_students))

name_starts_with_m = lambda student: str(student[0]).startswith(('m', 'M')) 
students_with_m_names = filter(name_starts_with_m, students)
print('Students with names that start with "m":', list(students_with_m_names))