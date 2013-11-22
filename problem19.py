# problem 19
# SOLVED

# count the number of Sundays that are the first of the month
counter = 0
# start with Tuesday Jan 01, 1901
dayoftheweek = 2

# go through each year from 1901 to 2000
for x in xrange(1901,2001):
	# if not a leap year	
	if x%4 != 0 or x%400 == 0:
		# go through each month 1 to 12
		for y in xrange(1,13):
			# if month is April, June, September, or November
			if y == 4 or y == 6 or y == 9 or y == 11:
								
				for z in xrange(1,31):
					if z == 1 and dayoftheweek == 7:
						counter += 1
						print "year: " + str(x) + " month: " + str(y)
					dayoftheweek += 1
					if dayoftheweek == 8:
						dayoftheweek = 1
				
			# if February
			elif y == 2:
								
				for z in xrange(1,29):
					if z == 1 and dayoftheweek == 7:
						counter += 1
						print "year: " + str(x) + " month: " + str(y)
					dayoftheweek += 1
					if dayoftheweek == 8:
						dayoftheweek = 1
			# any other month			
			else:
							
				for z in xrange(1,32):
					if z == 1 and dayoftheweek == 7:
						counter += 1
						print "year: " + str(x) + " month: " + str(y)
					dayoftheweek += 1
					if dayoftheweek == 8:
						dayoftheweek = 1
			
	# if leap year
	else:
		# go through each month 1 to 12
		for y in xrange(1,13):
			# if month is April, June, September, or November
			if y == 4 or y == 6 or y == 9 or y == 11:
								
				for z in xrange(1,31):
					if z == 1 and dayoftheweek == 7:
						counter += 1
						print "year: " + str(x) + " month: " + str(y)
					dayoftheweek += 1
					if dayoftheweek == 8:
						dayoftheweek = 1
				
			# if February
			elif y == 2:
								
				for z in xrange(1,30):
					if z == 1 and dayoftheweek == 7:
						counter += 1
						print "year: " + str(x) + " month: " + str(y)
					dayoftheweek += 1
					if dayoftheweek == 8:
						dayoftheweek = 1
			# any other month			
			else:
							
				for z in xrange(1,32):
					if z == 1 and dayoftheweek == 7:
						counter += 1
						print "year: " + str(x) + " month: " + str(y)
					dayoftheweek += 1
					if dayoftheweek == 8:
						dayoftheweek = 1

print "Total first sundays: " + str(counter)






