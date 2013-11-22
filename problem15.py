# problem 15
import util
import sys

sys.setrecursionlimit(10000000)
cache = {}

def countpaths ( width, height ):
	paths = 0
	if width > 1 and height > 1:
		paths = countpaths(width, height - 1) + countpaths(width - 1, height)
	elif width == 1:
		paths = height + 1
	elif height == 1:
		paths = width + 1
	return paths
		


# print countpaths (20, 20)
print util.Factorial(40)/util.Factorial(20)/util.Factorial(20)

