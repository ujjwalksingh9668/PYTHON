# Q-Given the names and grades for each student in a class of  students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

#Solution:-
students = []

n = int(input())

for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

grades = sorted({grade for name, grade in students})
second_lowest = grades[1]

result = [name for name, grade in students if grade == second_lowest]

result.sort()

for name in result:
    print(name)
