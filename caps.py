fname = input('enter file name:')
try:
    fhand = open(fname)
except:
    print('file cannot be opened')
    exit()
for line in fhand:
	shout = line.rstrip().upper()
	print(shout)