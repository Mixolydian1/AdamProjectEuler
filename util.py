import math

# takes a number i.e. 1234567890 and returns an array representing the number in the form of
# [ones, tens, hundreds, etc.]
def NumberToArray (x):
	array = []
	while x > 0:
		array.append(x%10)
		x = x / 10
	return array

# takes two arrays, each of ints, and returns the sum in array form
#not working
def AddArrays (x, y):
	array = []	
	a = len(x)
	b = len(y)
	if a > b:
		largerlength = a
	else:
		largerlength = b
	for x in xrange(0,largerlength):
		print "a"
	return array	

# returns the factorial of a number
def Factorial (n):
	factorial = 1	
	for x in xrange (1, n+1):
		factorial = factorial * x
	return factorial


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

# returns solutions to the equation ax^2 + bx + c = 0
# if there are no real solutions, returns None
def quadratic (a, b, c):
	answers = None 	
	discriminant = 	b*b - 4*a*c
	if discriminant >= 0:
		x1 = (-1*b + math.sqrt(discriminant)) / 2*a
		x2 = (-1*b - math.sqrt(discriminant)) / 2*a
		answers = x1, x2
	return  answers

# returns the positive solution to a quadratic expression
def pos_quadratic (a, b, c):
	answer = None
	discriminant = 	b*b - 4*a*c
	if discriminant >= 0:
		x1 = (-1*b + math.sqrt(discriminant)) / 2*a
		x2 = (-1*b - math.sqrt(discriminant)) / 2*a
		
	return  answer

