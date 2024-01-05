# Problem: https://adventofcode.com/2023/day/2
#This solution WORKS!

import re

suffix = ''
nest = []
running = []

#double checks if the indicies are in bounds
def valid(row, col):
	return (0 <= row < len(nest)) and (0 <= col < len(nest[0]))

# Check if the element is a symbol (non-digit, non-period, non-newline)
def is_symbol(char):
        return char.isascii() and not char.isdigit() and char != '.' and char !='\n'


def touches_symbol(row, start, end):
    # Iterate over a block one row before, one row after, and to the left and right 
    for r in range(max(row-1,0), min(row + 2, len(nest))):
        for c in range(max(start-1,0), min(end + 1, len(nest[r]))):
            # Check if the current position (r, c) is valid
            if valid(r, c):
                if is_symbol(nest[r][c]):
                    #print("Found a symbol at: ",  r+1," ", c,  "\t",nest[r][c],  end='\t')
                    return True  #I found a symbol!
    return False  #no symbol found	

with open('input'+suffix+'.txt', 'r') as imp:
	for l in imp:
		nest.append(l)

def collect():
	nummatch = re.compile(r'(\d+)')
	for row, n in enumerate(nest):
		for match in re.finditer(nummatch, n):
			
			if touches_symbol(row, match.start(), match.end()):
				running.append(int(match.group(0)))
			#print(match.group(0))
	return running

final = collect()
print(final)
print("The sum of the parts is: ", sum(final))
