# Consider a list (list = You can perform the following
# commands:
# I. insert i e: Insert integer e at position i.
# 2. print: Print the list.
# 3.
# remove e: Delete the first occurrence of integer e..
# 4. append e: Insert integer e at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of
# commands where each command will be of the 7 types listed above
# Iterate through each command in order and perform the
# corresponding operation on your list.

#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

#Solution:-
import random,itertools
 
lst = []

for i in itertools.cycle([1]):
    command = input().split()
    if command[0] == "insert":
        i = int(command[1])
        e = int(command[2])
        lst.insert(i, e)
    elif command[0] == "print":
        print(lst)
    elif command[0] == "remove":
        e = int(command[1])
        lst.remove(e)
    elif command[0] == "append":
        e = int(command[1])
        lst.append(e)
    elif command[0] == "sort":
        lst.sort()
    elif command[0] == "pop":
        lst.pop()
    elif command[0] == "reverse":
        lst.reverse()
    elif command[0] == "stop":
        break
