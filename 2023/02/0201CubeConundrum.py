#Problem: https://adventofcode.com/2023/day/2
import re

running = 0
#Restriction: max cubes for red, blue and green, given by the problem
maxred = 12
maxgr = 13
maxbl = 14

game = re.compile(r'^Game (\d+):')
red = re.compile(r'(\d+) red')
green = re.compile(r'(\d+) green')
blue = re.compile(r'(\d+) blue')

with open('input.txt', 'r') as imp:
	for line in imp:
		#extract the game number and all the cube amounts
		glist = game.findall(line)
		redlist = red.findall(line)
		grlist = green.findall(line)
		bllist = blue.findall(line)
		r = 0
		g = 0
		b = 0
		#find the numerical maximum in each list
		for i in redlist:
			if int(i) > r: r = int(i)
		for i in grlist:
			if int(i) > g: g = int(i)
		for i in bllist:
			if int(i) > b: b = int(i)
		print(r, " red ", g, " green ", b, " blue")
		#check if the max cubes on the line fits in the Restriction
		if ((r <= maxred) and (g <= maxgr) and (b <= maxbl)): running += int(glist[0])
print("Final total is: ", running)

