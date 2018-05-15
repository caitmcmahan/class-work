mydict = ()
count = 0
fhand = open('mbox-short.txt')
for line in fhand:
	words = line.split()
	if len(words) == 0 or words[0] != 'From' : continue
	print(words[2])
	count = count + 1
for key in mydict:
	if mydict[keys] > 30 :
		print(key, mydict[key])
	print(count)