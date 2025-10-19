text = input('Введите английский текст с точкой на конце:')

while '.' not in text:
    text = input('Введите английский текст заново с точкой на конце:')

right_text = ''
correct_text = []

upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'

count = 0

for letter in text:
    if letter == '.':
        right_text += '.'
        correct_text.append(right_text)
        right_text = ''
    elif letter not in upper_alphabet and letter not in lower_alphabet and letter not in ' ,':
        right_text += ' '
    else:
        right_text += letter
        count += 1
    if count == 20:
        right_text += ' '
        count = 0

text = correct_text[0]

print('текст в правильном виде: ',text)

word = ''
words = []

for s in text:
    if s == ' ' or s == ',':
        words.append(word)
        word = ''
    else:
        word += s
if word != '':
    words.append(word)

k = 0

for w in words:
    if len(w)>k and w != '.':
        k = len(w)

kod = ''

count1 = 0

for i in text:

    for j in range(len(upper_alphabet)):
        if i == upper_alphabet[j]:
            if j+k<len(upper_alphabet):
                kod += upper_alphabet[j+k]
            else:
                kod += upper_alphabet[j+k-len(upper_alphabet)]
        elif i == lower_alphabet[j]:
            if j+k<len(lower_alphabet):
                kod += lower_alphabet[j+k]
            else:
                kod += lower_alphabet[j+k-len(upper_alphabet)]
        elif i not in lower_alphabet and i not in upper_alphabet and count1==0:
            kod += i
        count1 += 1

    count1 = 0

print('зашифрованный текст ',kod)
print('k = ',k)

