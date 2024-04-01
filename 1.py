print("Hello")


c = 14

n = int(input())

student = {}

for i in range(n):
    name, *marks = input().split()
    marks = list(map(float, marks))
    student[name] = marks

query_name = input()

average_marks = sum(student[query_name]) / len(student[query_name])

print("{:.2f}".format(average_marks))
