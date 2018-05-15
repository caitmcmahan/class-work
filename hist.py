fname = input('enter file:')
try:
	fhand = open(fname)
except:
	print('file cannot be opened:', fname)
	exit()
mbox = dict()
count = 0
for line in fhand:
	words = line.split()
	if (len(words)) == 0 or len(words) < 2 or words[0] != 'From' : continue
	else:
			if words[1] not in mbox:
				mbox[words[1]] = 1
			else:
				mbox[words[1]] += 1
print(mbox)