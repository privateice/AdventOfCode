#Problem: https://adventofcode.com/2023/day/1

import re

running = 0

with open('input.txt', 'r') as imp:
	for line in imp:
		first = ''
		last = ''
		ffound = True
		#check each character, save if its a digit, else skip
		for c in line:
			if not(c.isdigit()): continue
			if ffound:
				first = c
				ffound = False
			else:
				last = c
		#concatenate first and last. If there's no last, repeat first 2x
		first = first + (last if (last !='') else first)
		print("The calibration value is: ", first)
		running += int(first)
			
print("Final total is: ", running)

			
		