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
toRemove = []
for word in listText:
    if word in removeSentences:
        toRemove.append(word)
for remove in toRemove:
    listText.remove(remove)
print(';'.join(listText))