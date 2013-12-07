# Problem 14

# 1 					1
# 2 1					2
# 3 10 5 16 8 4 2 1			8
# 4 2 1					3
# 5 16 8 4 2 1				6
# 6 3 10 5 16 8 4 2 1			9
# 7 22 11 34 17 54 27 82 41 124 62 31 92 46 23 

import sys
sys.setrecursionlimit(100000)

# retuns the number of terms of the Collatz sequence that starts with the integer "num"
def collatz (num):
	if num<0:
		raise ValueError("Passed a number less than 0")
	answer = 0
	if num == 1:
		answer = 1
	elif num in cache:
		answer = cache[num]
	else:
		if num%2 == 0:
			answer = 1 + collatz(num/2)
		else:
			answer = 1 + collatz(num*3+1)
	return answer

cache = {}
largest = 0
giveslargest = 0
bound = 1000000


for x in xrange(1,bound):
	cache[x] = collatz(x)

"""
print cache

"""


for x in xrange(1,bound):
	if cache[x] > largest:
		largest = cache[x]
		giveslargest = x

print "The number that gives the largest Collatz sequence is : " + str(giveslargest)
print "The largest Collatz sequence has this many terms: " + str(largest)


"""
print cache[35655]
print cache[837799]
"""


