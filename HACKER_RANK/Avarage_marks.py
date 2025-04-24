#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
# Print the average of the marks array for the student name provided,
# showing 2 places after the decimal.
#Sample Input 0
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Sample Output 0
#
# 56.00
# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

# Solution:-
n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    score = list(map(float,line))
    student_marks[name]= score
query_name = input()
print(format(sum(student_marks[query_name])/len(student_marks[query_name]),".2f"))
