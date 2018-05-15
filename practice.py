total = 0
count = 0
average = 0
while True:
    inp = input('Enter a number:')
    if inp == "done":
        break
    try:
        x = float(inp)
    except:
        print('Invalid input')
        continue
    total = total + x
    count = count + 1
    average = total / count
print('Count of variables in list is', count, 'variables')
print('Sum of variables in list is', total,)
print('Average of variables in list is', average,)