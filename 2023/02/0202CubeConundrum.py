#Problem: https://adventofcode.com/2023/day/2
import re

running = 0

red = re.compile(r'(\d+) red')
green = re.compile(r'(\d+) green')
blue = re.compile(r'(\d+) blue')

with open('input.txt', 'r') as imp:
	for line in imp:
		#Extract the cube amounts
		redlist = red.findall(line)
		grlist = green.findall(line)
		bllist = blue.findall(line)
		r = 0
		g = 0
		b = 0
		#Find the numerical maximum for each color
		for i in redlist:
			if int(i) > r: r = int(i)
		for i in grlist:
			if int(i) > g: g = int(i)
		for i in bllist:
			if int(i) > b: b = int(i)
		#print(r, " red ", g, " green ", b, " blue")
		#print("power is: ", r * g * b)
		#Add the power to the running total
		running += (r * g * b)
print("Final total is: ", running)

