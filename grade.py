grade = input('enter score:')
try:
   g = float(grade)
except:
    print('Bad score')
    quit()
if g > 1.0:
    print('Bad score')
elif g >= 0.9:
    print('A')
elif g >= 0.8:
    print('B')
elif g >= 0.7:
    print('C')
elif g >= 0.6:
    print('D')
elif g <= 0.5:
    print('F')
else:
    print('Bad score')