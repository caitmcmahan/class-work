fname = input('enter file:')
try:
	fhand = open(fname)
except:
	print('file cannot be opened:', fname)
	exit()
receip = dict()
count = 0
for line in fhand:
	words = line.split()
	if (len(words)) == 0 or len(words) < 2 or words[0] != 'From' : continue
	else:
			atposition = words[1].find('@')
			domain = words[1][atposition+1:]
			if domain not in receip:
				receip[domain] = 1
			else:
				receip[domain] += 1
			print(receip)