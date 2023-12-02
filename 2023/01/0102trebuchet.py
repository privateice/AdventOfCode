#Problem: https://adventofcode.com/2023/day/1

import re

digstr = {	"one": '1', "two":'2',"three":'3',
			"four":'4',"five":'5',"six":'6',
			"seven":'7',"eight":'8',"nine":'9',
			"1":'1',"2":'2',"3":'3',"4":'4',"5":'5',
			"6":'6',"7":'7',"8":'8',"9":'9'}
running = 0

digits = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
 
with open('input.txt', 'r') as imp:
	for line in imp:
		#Use regex to find all the digits and digit-words
		lmatch = digits.findall(line)
		#print(lmatch)
		#concatenate and extract
		if len(lmatch) == 1:  #the first digit twice
			calVal = digstr[lmatch[0]] + digstr[lmatch[0]]
		else: #the first and last digits
			calVal = digstr[lmatch[0]] + digstr[lmatch[-1]]
		#print("The calibration value is: ", calVal)
		running += int(calVal)
			
print("Final total is: ", running)

			
		