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
    "under",
    "selective",
    "over"
]

loop = 1
while loop:
	text = input("Input the text:")
	if not text:
		loop = 0
		continue
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
print('operação finalizada')
