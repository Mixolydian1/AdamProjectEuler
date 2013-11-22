# problem 16
# SOLVED

number = 1
for x in xrange(1,1001):
	number = number * 2

print number
total = 0

while number > 0:
	total += number%10
	number /= 10
	

print total

# alteratively

print sum([int(x) for x in str(2**1000)])
