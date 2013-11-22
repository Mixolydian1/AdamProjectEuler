# Problem 20
# SOLVED

number = 1
for x in xrange(1,101):
	number = number*x

print number
	
total = 0

while number > 0:
	a = number%10
	total = total + a
	number = number/10

print total
