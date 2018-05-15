sonnet = []
fhand = open('romeo.txt')
for line in fhand:
	words = line.split()
	for word in words:
		sonnet.append(word)
print(sorted(sonnet))