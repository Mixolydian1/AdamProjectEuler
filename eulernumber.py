# Euler's number
import math
import decimal

decimal.getcontext().prec = 200

bound = 100
total = 0
for x in xrange(0,bound):
	total += decimal.Decimal(1)/math.factorial(x)
	if x == bound - 1:	
		print "Term(" + str(x) + "): " + str(total)

print decimal.Decimal((1+decimal.Decimal(1)/(bound-1))**(bound-1))
