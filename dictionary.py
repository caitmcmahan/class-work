count = 0
eng2deutsch = dict()
eng2deutsch = {'one' : 'eins' , 'two' : 'zwei' , 'three' : 'drei'}
fhand = open('words.txt')
for line in fhand:
	words = line.split()
	for word in words:
		count = count + 1
	if word in eng2deutsch : continue
	eng2deutsch[word] = count
inp = input('check:')
if inp in eng2deutsch:
	print('True')
else:
	print('False')