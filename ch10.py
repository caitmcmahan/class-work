import string

fname = input('enter file name:')
try:
	fhand = open(fname)
except:
	print('File cannot be opened', fname)
	exit()
	
count = 0
counts = dict()

for line in fhand:
	line = line.translate(str.maketrans('', '', string.punctuation))
	line = line.translate(str.maketrans('', '', string.digits))
	line = line.upper()
	line = line.lower()
	words = line.split()
	for word in words:
		for letter in word:
			count += 1
		if letter not in counts:
			counts[letter] = 1
		else:
			counts[letter] += 1
			
lst = list()
for key, val in list(counts.items()):
	lst.append((val, key))
	
lst.sort(reverse = True)

for key, val in lst:
	print(key, val)