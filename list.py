thelist = []
while (True):
	inp = input('enter number:')
	if inp == 'done' : break
	thelist.append(inp)
print('Max:', max(thelist))
print('Min:', min(thelist))