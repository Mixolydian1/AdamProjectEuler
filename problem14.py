# Problem 14

import sys
sys.setrecusrionlimit(100000)

# retuns the number of terms in a Collatz sequence with starting number "num"
def Collatz (num):
	answer = 0
	if num == 1:
		answer = 1
	elif num in cache:
		answer = cache[num]
	else:
		if num%2 == 0:
			answer = 1 + cache[num/2]
			else
						
				

cache = {}
giveslargest = 1
mostpaths = 0
bound = 25

for x in xrange(0,21):
	cache[2**x] = x + 1
	

for x in xrange(1,bound):
	key = x
	if key in cache:
		continue
	else:
		continue

print cache


