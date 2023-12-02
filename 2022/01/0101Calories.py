#https://adventofcode.com/2022/day/1
f = open('input.txt')
current = 0
currentelf = 0
maxcal = 0
maxelf = 0
for x in f:
	if x == '\n':
		currentelf+= 1
		print("current elf is ", currentelf, " with ", current, " calories.")
		if current > maxcal:
			maxelf = currentelf
			maxcal = current
			
		current = 0
		continue
		
	current += int(x)
		
	
	#print("current elf is ", currentelf, " with ", current, " calories.")
	
print("The elf with the most calories is #",maxelf , " with " , maxcal , " calories." )
f.close()