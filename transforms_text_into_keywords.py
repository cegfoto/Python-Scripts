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
	"over",
	"against",
	"down",
	"known",
	"as",
	"amid",
	"amidst"
]

genericKeywords = {
	"food": [
		"taste",
		"meal"
	],
	"mushroom": [
		"fungus",
		"fungi",
		"organic"
	],
	"texture": [
		"surface",
		"material"
	],
	"plant": [
		"flora",
		"nature",
		"natural",
		"botany",
		"biology",
		"seasonal",
		"organic"
	],
	"plants": [
		"flora",
		"nature",
		"natural",
		"botany",
		"biology",
		"seasonal",
		"organic",
		"plant"
	],
	"sky": [
		"air",
		"high",
		"atmosphere",
		"climate",
		"heaven",
		"meteorology",
		"weather"
	],
	"cloud": [
		"air",
		"climate",
		"clouds",
		"cloudscape",
		"meteorology",
		"weather",
		"fluffy"
	],
	"clouds": [
		"air",
		"climate",
		"clouds",
		"cloudscape",
		"meteorology",
		"weather",
		"fluffy",
		"cloud"
	],
	"meat": [
		"protein"
	],
	"dairy": [
		"food",
		"nutrition",
		"product",
		"cuisine",
		"milk",
		"gastronomy"
	],
	"game": [
		"editorial",
		"entertainment",
		"gaming",
		"play",
		"hobbie"
	],
	"leaf": [
		"nature",
		"natural",
		"season",
		"plant",
		"organic"
	],
	"leaves": [
		"nature",
		"natural",
		"season",
		"plant",
		"leaf",
		"foliage",
		"organic"
	],
	"ingredient": [
		"food",
		"cook",
		"cooking",
		"meal",
		"dish",
		"gourmet",
		"tasty",
		"lunch",
		"dinner",
		"delicious",
		"gastronomy",
		"condiment"
	],
	"wildlife": [
		"nature",
		"natural",
		"animal",
		"fauna",
		"wild",
		"biology",
		"habitat",
		"environment",
		"organic"
	],
	"falling": [
		"movement",
		"fall"
	],
	"trees": [
		"nature",
		"natural",
		"plant",
		"flora",
		"biology",
		"seasonal",
		"wood",
		"tree"
	],
	"tree": [
		"nature",
		"natural",
		"plant",
		"flora",
		"biology",
		"seasonal",
		"wood"
	],
	"treetop": [
		"branch",
		"natural",
		"nature",
		"plant",
		"flora",
		"tree",
		"season",
		"biology",
		"seasonal"
	],
	"rice": [
		"grain",
		"meal",
		"food",
		"gastronomy",
		"nutrition",
		"tasty",
		"ingredient",
		"organic"
	],
	"flower": [
		"nature",
		"natural",
		"plant",
		"season",
		"flora",
		"biology",
		"botanical",
		"floral",
		"seasonal",
		"petal",
		"organic"
	],
	"flowers": [
		"nature",
		"natural",
		"plant",
		"season",
		"flora",
		"biology",
		"botanical",
		"floral",
		"seasonal",
		"petal",
		"flower",
		"organic"
	],
	"fruit": [
		"agriculture",
		"nutrition",
		"natural",
		"organic",
		"food",
		"harvest",
		"taste"
	],
	"vegetable food": [
		"agriculture",
		"nutrition",
		"natural",
		"organic",
		"food",
		"harvest",
		"taste",
		"horticultural"
	],
	"bird": [
		"animal",
		"fauna",
		"biology",
		"birdwatching"
	],
	"birds": [
		"animal",
		"fauna",
		"biology",
		"bird",
		"birdwatching"
	],
	"sauce": [
		"food",
		"cook",
		"cooking",
		"meal",
		"dish",
		"gourmet",
		"tasty",
		"lunch",
		"dinner",
		"delicious",
		"gastronomy"
	],
	"dish": [
		"food",
		"cook",
		"cooking",
		"meal",
		"dish",
		"gourmet",
		"tasty",
		"lunch",
		"dinner",
		"delicious",
		"gastronomy"
	],
	"cooking": [
		"food",
		"cook",
		"dish",
		"meal",
		"gourmet",
		"tasty",
		"lunch",
		"dinner",
		"delicious"
	],
	"water": [
		"wet",
		"liquid",
		"aqua",
		"texture"
	],
	"life": [
		"biology"
	],
	"blurred": [
		"blur",
		"bokeh",
		"defocused",
		"focus"
	],
	"moon": [
		"satellite",
		"space",
		"universe",
		"crater"
	]
}



compoundWords = [
	"close up",
	"bell pepper",
	"ground beef",
	"vegetable food",
	"passion fruit"
];

def getWordsFromTitle(text):
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
	return listText
	
def verifyCompoundWords(text):
	usedCompCompoundWords = []
	for word in compoundWords:
		if text.find(word) >= 0:
			usedCompCompoundWords.append(word)
			text = text.replace(word, '')
	return [usedCompCompoundWords,text]

def associateKeywords(arrayText):
	for word in genericKeywords.keys():
		if word in arrayText:
			arrayText += genericKeywords[word]
	arrayText = list(dict.fromkeys(arrayText))
	return arrayText
	

loop = 1
while loop:
	text = input("Input the text:")
	#to test:
	#text = 'bell pepper in the table of the dinner with food and rice and plant' 
	if not text:
		loop = 0
		continue
	compoundWordsFinded = verifyCompoundWords(text)
	arrayText = compoundWordsFinded[0]
	text = compoundWordsFinded[1]
	text = text.strip()
	listText = getWordsFromTitle(text)
	arrayText = arrayText + listText
	option = input("Do you want to add keywords associated with the words in the title?")
	if option:
		arrayText = associateKeywords(arrayText)
	arrayText.append('nobody')
	print(';'.join(arrayText))
print('operação finalizada')
