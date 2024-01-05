import re
suffix = ''

running = 0
with open('input' + suffix + '.txt','r') as imp:
	for line in imp:
		winners = []
		mines = []
		c, w, m = re.split(r'[:|]', line)
		#print(c, w, m)
		junk, card = c.split()
		winners = w.split()
		mines = m.split()
		#print(card, winners, mines)
		count = 0
		for m in mines:
			if m in winners:
				count += 1
		if count > 0:
			running += 2 ** (count - 1)
			
print(running)