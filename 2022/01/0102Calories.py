#https://adventofcode.com/2022/day/1
f = open('input.txt')
current = 0
currentelf = 0
maxcal = 0
maxelf = 0
seccal = 0
secelf = 0
thirdcal = 0
thirdelf = 0
for x in f:
	#print(x)
	if x == '\n':
		currentelf+= 1
		print("current elf is ", currentelf, " with ", current, " calories.")
		if current > thirdcal:
			thirdelf = currentelf
			thirdcal = current
			
		if current > seccal:
			thirdelf = secelf
			thirdcal = seccal
			secelf = currentelf
			seccal = current

		if current > maxcal:
			thirdelf = secelf
			thirdcal = seccal
			secelf = maxelf
			seccal = maxcal
			maxelf = currentelf
			maxcal = current
			print("The elf with the 3rd most calories is #", thirdelf , " with " , thirdcal , " calories." )
			print("The elf with the 2nd most calories is #",secelf , " with " , seccal , " calories." )
			print("The elf with the most calories is #",maxelf , " with " , maxcal , " calories." )
		current = 0
		continue
		
	current += int(x)
		
	
	#print("current elf is ", currentelf, " with ", current, " calories.")

print("The elf with the 3rd most calories is #", thirdelf , " with " , thirdcal , " calories." )
print("The elf with the 2nd most calories is #",secelf , " with " , seccal , " calories." )
print("The elf with the most calories is #",maxelf , " with " , maxcal , " calories." )
print("the total calories the top 3 are carrying is ", maxcal+seccal+thirdcal)
f.close()