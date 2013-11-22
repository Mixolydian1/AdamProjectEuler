# Problem 2

a = 1
b = 2
total = 2
h = 0
while h <= 4000000:
	h = a + b
	#print "h: " + str(h)
	if h%2 == 0:
		total += h
		
	a = b
	b = h
	#print "b: " + str(b)
	
	#print "a: " + str(a)

print total
