hours = input('enter hours:')
try:
    hrs = int(hours)
except:
    print('error: please enter numeric input')
    quit()
rate = input('enter rate:')
try:
    r = float(rate)
except:
    print('error: please enter a numeric input')
if hrs > 40:
    pay = (hrs - 40) * (r * 1.5) + (40 * r)
    print(pay)
else:
    def computepay():
        pay = hrs * r
print(pay)