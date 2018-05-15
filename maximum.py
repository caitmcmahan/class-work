largest = None
smallest = None
x = None
while True:
    inp = input('enter number:')
    if inp == "done":
        break
    try:
        x = float(inp)
    except:
        print ('Invalid input')
        continue
    if largest is None or x > largest:
        largest = x
    if smallest is None or x < smallest:
        smallest = x
    print('Maximum is', largest)
    print('Minimum is', smallest)