n = int(input())
students = []

for i in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

students.sort(key=lambda x: x[1])

second_grade = sorted(set(score for name, score in students))[1]

for name, score in sorted(students):
    if score == second_grade:
        print(name)