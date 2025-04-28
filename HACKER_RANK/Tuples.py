# Q-Given an integer. n. and n space-separated integers as input. create a
# tuple. t. of those n integers. Then compute and print the result of
# hash(t).
# Note: hash() is one of the functions in the
# _ bui Iti ns__ module. so it
# need not be imported.
#https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true

# Solution:-
n = int(input())
integer_list = map(int,input().split())
t = tuple(integer_list)
print(hash(t))
