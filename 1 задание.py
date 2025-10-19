text = input('введите текст через пробел: ')

word = ''
words = []

for s in text:
    if s == ' ':
        words.append(word)
        word = ''
    else:
        word += s
if word:
    words.append(word)

reverse_words1 = []
reverse_words2 = []
reverse_word2 = ''

for k1 in range(len(words)-1,-1,-1):
        reverse_words1.append(words[k1])

for w2 in reverse_words1:

    for k2 in range(len(w2)-1,-1,-1):
        reverse_word2 += w2[k2]

    reverse_words2.append(reverse_word2)
    reverse_word2 = ''

reverse_sentence1 = ''
reverse_sentence2 = ''

for el1 in reverse_words1:
    reverse_sentence1 += el1
    reverse_sentence1 += ' '

for el2 in reverse_words2:
    reverse_sentence2 += el2
    reverse_sentence2 += ' '

print(text, ' - ', reverse_sentence1)
print(text, ' - ', reverse_sentence2)











