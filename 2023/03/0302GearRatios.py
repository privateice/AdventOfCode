# Problem: https://adventofcode.com/2023/day/2
#The answer is 530495
nest = []
suffix = ''
with open('input'+suffix+'.txt', 'r') as imp:
	for l in imp:
		nest.append(list(l))

def valid(row, col):
	return (0 <= row < len(nest)) and (0 <= col < len(nest[0]))

def is_symbol(char):
        return char.isascii() and not char.isdigit() and char != '.' and char !='\n'

def is_digit(char):
	return char.isdigit()

def get_num(r, c):
	num_str = ''
	
	# Move to the left until a non-digit character is found or the beginning is reached
	i = 0
	while valid(r, c + i) and nest[r][c + i].isdigit():
		num_str = nest[r][c + i] + num_str
		nest[r][c + i] = '.'
		i -= 1

	# Move to the right until a non-digit character is found or the end is reached
	i = 1
	while valid(r, c + i) and nest[r][c + i].isdigit():
		num_str += nest[r][c + i]
		nest[r][c + i] = '.'
		i += 1

	#print(num_str, end='\t')
	return int(num_str)

def get_numbers_around(row, col):
	adj = []
	
	for i in range(-1, 2):
		for j in range(-1, 2):
			if i == 0 and j == 0:
				continue  # Skip the current cell
			nrow, ncol = row + i, col + j
			if valid(nrow, ncol) and is_digit(nest[nrow][ncol]):
				adj.append(get_num(nrow, ncol))
	return adj

def collect():
	result = []
	for r in range(len(nest)):
		#print()
		for c in range(len(nest[0])):
			curr = nest[r][c]
			if is_symbol(curr):
				#print("Found a symbol at: ", r+1, c, "\t", curr, end="\t")
				adj = get_numbers_around(r, c)
				#print(adj)
				if adj and len(adj) == 2:
					result.append(adj[0]*adj[1])
					
	
	return result

final = collect()
#print(final)
print("The sum of the parts is: ", sum(final))
