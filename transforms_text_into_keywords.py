removeSentences = [
    "of",
    "the",
    "and",
    "in",
    "with",
    "above",
    "among",
    "on",
    "a",
    "under"
]

text = input("Input the text:")
text = text.replace(',', '')
text = text.replace('.', '')
listText = text.split(' ')
listText = list(dict.fromkeys(listText))
for word in listText:
    if word in removeSentences:
        listText.remove(word)
print(';'.join(listText))