
suffix = ''
seeds = []
maps = {'seed-to-soil':[],
		'soil-to-fertilizer':[],
		'fertilizer-to-water':[],
		'water-to-light':[],
		'light-to-temperature':[],
		'temperature-to-humidity':[],
		'humidity-to-location':[]
		}
answers = {'seeds':[],
		'seed-to-soil':[],
		'soil-to-fertilizer':[],
		'fertilizer-to-water':[],
		'water-to-light':[],
		'light-to-temperature':[],
		'temperature-to-humidity':[],
		'humidity-to-location':[]
		}

with open('input' + suffix + '.txt','r') as imp:
	cont = imp.readlines()
	
#Get list of seeds
j, s = cont[0].split(r':')
seeds = [int(x) for x in s.split()]
print(seeds)

#Process the file's lines
j = 2
ckey = ''
while j < len(cont):
	if cont[j] == '\n': j += 1
	if not cont[j][0].isdigit(): 
		ckey = cont[j].rstrip(' map:\n')
	else: 
		maps[ckey].append([int(x) for x in cont[j].split()])
	j += 1
'''
for k in maps.keys():
	print("Key: ", k)
	for l in maps[k]:
		print("\t", l)
'''
ds = 0 #destination range start
ss = 1 #source range start
rl = 2 #range length
for s in seeds:
	print("Seed: ", s)
	answers['seeds'].append(s)
	for k in maps.keys():
		found = False
		print("\tKey: ", k)
		for l in maps[k]:
			r = range(l[ss], l[ss] + l[rl] + 1)
			#print("\t\t\t", l[ss], l[ss] + l[rl])
			if s in r:
				s = l[ds] + r.index(s)
				answers[k].append(s)
				print("\t\t\t", s)
				found = True
				break
		if not found:
			print("\t\t\t", s)
			answers[k].append(s)
#next step, if l is in the range, figure out where it is and what the destination is

m = min(answers['humidity-to-location'])
mi = answers['humidity-to-location'].index(m)

print("The nearest location is: ", m )
print("The closest seed is: ", answers["seeds"][mi])