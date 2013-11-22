# problem 27
import math

# determines if a number is prime
def isPrime(num):
	prime = True
	if num == 1:
		prime = False
	elif num > 2 and num%2 == 0:
		prime = False
	else:
		for x in xrange(3, int(math.floor(math.sqrt(num)))+1):
			if num%x == 0:
				prime = False

	return prime
		
total = 0
for x in xrange(1,100):
	if isPrime(x):
		print x
		total += 1
print "total: " + str(total)



"""
for x in xrange(0, int(math.floor(math.sqrt(15)))):
	print "a"
print math.sqrt(14)
"""
