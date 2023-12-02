#https://adventofcode.com/2022/day/4
f = open('input.txt')
counter = 0
for x in f:
	(elf1, elf2) = x.split(",")
	(elf1Low, elf1High) = elf1.split("-")
	(elf2Low, elf2High) = elf2.split("-")
	elf1Low = int(elf1Low)
	elf1High = int(elf1High)
	elf2Low = int(elf2Low)
	elf2High = int(elf2High)	
	if not(elf1High < elf2Low or elf2High < elf1Low):
		counter += 1
	
	
print(counter, "elves overlap at all" )
f.close()