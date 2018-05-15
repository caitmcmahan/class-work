hours = input('enter hours:')
try:
    hrs = int(hours)
except:
    print('Error, please enter a numeric input')
    quit()
rate = input('enter rate:')
try:
    r = float(rate)
except:
    print('Error, please enter a numeric input')
    quit()
if hrs > 40:
    pay = (hrs - 40) * (r * 1.5) + (40 * r)
    print(pay)
else:
    pay = hrs * r
    print(pay)