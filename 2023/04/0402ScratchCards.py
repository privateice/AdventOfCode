import re

suffix = ''
winners = []
mine = []
cards = []
counts = []

with open('input' + suffix + '.txt','r') as imp:
	for line in imp:
		c, w, m = re.split(r'[:|]', line)
		#print(c, w, m)
		winners.append(w.split())
		mine.append(m.split())

#each line in mine has:
	#a count of winners for each card in counts 
	#and a number of cards owned in cards
counts = [0 for _ in range(len(mine))]
cards = [1 for _ in range(len(mine))]	
#count the winners for each card	
for i, m in enumerate(mine): #each line
	for n in range(len(m)): #each number in the line, except @ 0
		if m[n] in winners[i]:
			counts[i] += 1
#for each count of winners 
#for the first card, add 1 to each of the next c cards held
#the add cards[i] winners for each (c) of the counts
for i, c in enumerate(counts):
	for cp in range(c):
		cards[i + cp + 1] += 1 if i == 0 else cards[i]

print("The total of cards won is " , sum(cards))