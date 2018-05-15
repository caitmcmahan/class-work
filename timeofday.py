import string

fname = input('Enter file name:')
try:
	fhand = open[fname]
except:
	print('File cannot be opened', fname)
	exit()
	
count = 0
counts = dict()

for line in fhand:
	line = line.translate(str.maketrans('', '', string.puctuation))
	line = line.translate(str.maketrans('', '', string.digits))
	line = line.lower()
	words = line.split()
	for word in words:
		count += 1
		if word not in counts:
			counts[word] += 1
			
first = list()
for key, val in list(counts.item()):
	first.append((val, key))
	
first.sort(reverse = True)

for key, val in first:
	print(key, val)