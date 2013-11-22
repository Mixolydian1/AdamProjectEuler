# problem 45

#triangle = {}
#pentagonal = {}
#hexagonal = {}

# t = n(n+1)/2
# p = n(3n-1)/2
# h = n(2n-1)

notfound = True
tindex = 286
pindex = 165
hindex = 143
triangle = 0
pentagonal = 0
hexagonal = 0


while notfound:
	pindex = pstart
	hindex = hstart
	#triangle[tindex] = tindex(tindex + 1)/2
	#pentagonal[pindex] = pindex(3*pindex - 1)/2
	#hexagonal[hindex] = hindex(2*hindex - 1)	
	triangle = tindex*(tindex + 1)/2
	print "t: " + str(triangle)	
	while pentagonal < triangle:
		pentagonal = pindex*(3*pindex - 1)/2
		pindex += 1
		print "p: " + str(pentagonal)
		while hexagonal < pentagonal:
			hexagonal = hindex*(2*hindex - 1)
			hindex += 1
			print "h: " + str	
		
	if triangle == pentagonal and triangle == hexagonal:
		notfound = False
	tindex += 1
	
print "ANSWER: " + str(triangle)
