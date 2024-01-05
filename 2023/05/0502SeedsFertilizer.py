
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

with open('input' + suffix + '.txt','r') as imp:
	cont = imp.readlines()
	
#Get list of seeds
j, s = cont[0].split(r':')
seeds = [list(map(int, s.split()[2 * i:2 * i + 2])) for i in range(len(s.split()) // 2)]

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

ds = 0 #destination range start
ss = 1 #source range start
rl = 2 #range length
lowest = 0

def find_range_in_map(r,amap):
temp = []
#r is a list: start, length
#amap is a list of lists, each of which contains a range
		print(r)
		rs = 0
		rl = 1
		rstart = r[0]
		rend = r[0] + r[1]
		rlength = r[1]
	
		for l in amap:
			#r0 range start value, r1 range length
			#l0 destination start, l1 source start, l2 map length
			
			if rstart > l[1]:
				if rend < (l[1]+l[2]):
					#l1-------r0-----------ro+r1-----------l1+ll
					temp.append([l[0] + (r[0] - l[1]), r[1])
					print("Found")
			if rstart > l[1]:
				if rend > (l[1]+l[2]):
					#l1-------r0-------------l1+l2---------ro+r1
					temp.append([l[0] + (r[0] - l[1]), )
					print("Start is in range, but end is outside")
			if rend < (l[1]+l[2]):
				if rstart < l[1]:
					print("End is in the range but start is below")
			if rend > (l[1]+l[2]):
				if rstart < l[1]:
					print("The range is bigger than the map range")
					
find_range_in_map(seeds[0],maps['seed-to-soil'])
'''
for s in range(slist[0], slist[0] + slist[1] + 1):
	for k in maps.keys():
		found = False
		for l in maps[k]:
			r = range(l[ss], l[ss] + l[rl] + 1)
			if s in r:
				s = l[ds] + r.index(s)
				break
	lowest = s if (s < lowest) or (lowest == 0) else lowest

#next step, if l is in the range, figure out where it is and what the destination is

print("The nearest location is: ", lowest )
'''


