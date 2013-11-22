# problem15b
import sys

sys.setrecursionlimit(100000000)

def countpaths (x, y, width, height):
	paths = 0
	if x == width or y == height:
		paths = 1
	else:
		paths = countpaths(x+1, y, width, height) + countpaths(x, y+1, width, height)
	return paths

print countpaths(0,0,10,10)


