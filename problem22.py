# problem 22


def butcher (current_list, to_remove = ["\n", "\t", "{", "}", ",", "\"", "[", "]"]):
	new_list = []
	for each_line in current_list:
		for each_item in to_remove:
			while not each_line.find(each_item) == -1:
				index1 = each_line.find(each_item)
				if each_item == ",":
					each_line = each_line[:index1] + " " + each_line[1+index1:]
				else:
					each_line = each_line[:index1] + each_line[1+index1:]
		new_line = each_line 			
		new_list.append(new_line)
	new_list = filter(None, new_list)	
	return new_list

def alphanumber (letter):
	letter = letter.lower()	
	value = 0	
	if letter == "a":
		value = 1
	elif letter == "b":
		value = 2
	elif letter == "c":
		value = 3
	elif letter == "d":
		value = 4
	elif letter == "e":
		value = 5
	elif letter == "f":
		value = 6
	elif letter == "g":
		value = 7
	elif letter == "h":
		value = 8
	elif letter == "i":
		value = 9
	elif letter == "j":
		value = 10
	elif letter == "k":
		value = 11
	elif letter == "l":
		value = 12
	elif letter == "m":
		value = 13
	elif letter == "n":
		value = 14
	elif letter == "0":
		value = 15
	elif letter == "p":
		value = 16
	elif letter == "q":
		value = 17
	elif letter == "r":
		value = 18
	elif letter == "s":
		value = 19
	elif letter == "t":
		value = 20
	elif letter == "u":
		value = 21
	elif letter == "v":
		value = 22
	elif letter == "w":
		value = 23
	elif letter == "x":
		value = 24
	elif letter == "y":
		value = 25
	else:
		value = 26
	return value

def nametolist (name):
	letterlist = []	
	namelength = len(name)
	for x in xrange (0, namelength):
		letterlist.append(name[x])
	return letterlist

currentfile = open("names.txt")
nameslist = list(currentfile)
currentfile.close()

nameslist = butcher(nameslist)
nameslist = nameslist[0].split()
nameslist = sorted(nameslist)

#print nameslist
print len(nameslist)

total_score = 0
counter = 1
for each_name in nameslist:
	current_score = 0	
	current_name = nametolist(each_name)
	for each_letter in current_name:
		current_score = current_score + alphanumber(each_letter)
	current_score = current_score * counter
	total_score = total_score + current_score	
	counter += 1

print nameslist[5162]
print nametolist(nameslist[5162])
for each_letter in nametolist(nameslist[5162]):
	print alphanumber(each_letter)
print (26 + 21 + 12 + 13 + 1)*5163

print current_score


print total_score


##############

with open('names.txt','r') as f:
    data = f.readline()

names = [name.strip('"') for name in data.split(",")]
sorted_names = sorted(names)
name_values = [ sum ( [ ord(char) - 64 for char in name ] ) for name in sorted_names ]
name_position_values = [ (pos+1) * nv for pos, nv in enumerate(name_values) ]
total_sum = sum(name_position_values)

print "total_sum solution: " + str(total_sum)

for a, b in zip(sorted_names, nameslist):
	if a!=b:
		print a, b

print sorted_names[4444]
print nameslist[4444]

"""

# debug output
from pprint import pprint
#position, word value, position * word value, word
pprint(zip(xrange(1,len(names)+1),name_values,name_position_values,sorted_names))

"""
