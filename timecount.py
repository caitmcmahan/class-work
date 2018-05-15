fname = input('Enter file name:')
try:
	fhand = open(fname)
except:
	print('File cannot be opened:', fname)
	exit()
	
count = dict()

for line in fhand:
	words = line.split()
	if (len(words) -- 0 or words[0] != 'From') : continue
	else:
		colpos = words[5].find(':')
		time = words[5][colpos+0]
		if line not in count:
			count[time] = 1
		else:
			count[time] += 1
			
first = list()

for key, val in list (count.items()) :

	first.sort()

for key, val in first:
	print(key, val)