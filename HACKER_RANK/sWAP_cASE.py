# Q- You are given a string and your task is to swap cases. In other words.
# convert all lowercase letters to uppercase letters and vice versa.
# For Example:
# Www.HackerRank. com + WWW. hACKERrANK. COM
#https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

# Solution:-
def swap_case(s):
    return s.swapcase()

n = input()
result = swap_case(n)
print(result)


