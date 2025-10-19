text = input('Введите слова через пробел: ')

upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'

lower_text = ''

for i in text:
    if i in upper_alphabet:
        for index in range(26):
            if i == upper_alphabet[index]:
                lower_text += lower_alphabet[index]
    else:
        lower_text += i

word = ''
words = []

for i in lower_text:
    if i == ' ':
        words.append(word)
        word = ''
    else:
        word += i
if word:
    words.append(word)

word_dict = {}

for el in words:
    if el in word_dict:
        word_dict[el]+=1
    else:
        word_dict[el]=1

new_words = []
a = word_dict.items()

for item in a:
    new_words.append({'слово':item[0],
                      'кол-во вхождений':item[1]})

for i in range(len(new_words)):
    max_c = i
    for j in range(i+1, len(new_words)):
        if new_words[j]['кол-во вхождений'] > new_words[max_c]['кол-во вхождений']:
            max_c = j
    new_words[i],new_words[max_c] = new_words[max_c],new_words[i]

print('Самые частые слова')
count = 0
for i in new_words:
    if count<5:
        print(i['слово'],i['кол-во вхождений'])
    count += 1
