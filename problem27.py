# problem 27
# SOLVED
import math

# determines if a number is prime
def isPrime(num):
	prime = True
	
	if num <= 1:
		prime = False
	elif num > 2 and num%2 == 0:
		prime = False
	else:
		for x in xrange(3, int(math.floor(math.sqrt(num)))+1):
			if num%x == 0:
				prime = False

	return prime
		
def compute(n,a,b):
	return n*n + n*a + b



hitend = False
longest_run = 0
bound = 2000

for alpha in xrange(bound*-1,bound+1):
	for beta in xrange(bound*-1,bound+1):
		consec = 0		
		for x in xrange(0,beta):
			if isPrime(compute(x,alpha,beta)):
				consec += 1
			else:
				break
		if consec > longest_run:
			longest_run = consec
			print "longest run so far: " + str(longest_run)
			print "alpha: " + str(alpha) + " beta: " + str(beta)
			print "product: " + str(alpha*beta)



