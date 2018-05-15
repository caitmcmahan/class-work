def count(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    print(count)
word = input('enter word:')
letter = input('enter letter:')
count(word, letter)