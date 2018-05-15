def chop(t):
	del t[0]
	del t[-1]
letters = ['a', 'b', 'c', 'd']
letters1 = chop(letters)
print(letters1)
	