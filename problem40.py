# problem 40

# SOLVED

number = "1"
counter = 2
while len(number) < 1000001:
	number = number + str(counter)
	counter += 1

total = 1
for x in xrange(0,7):
	total *= int(number[10**x - 1])

print total

