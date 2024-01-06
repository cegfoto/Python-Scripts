import pandas as pd

# def getWordsFromTitle(text):
#     loop = 1
#     while loop:
#         text = input("Input the text:")
#         df = pd.read_csv('keywords.csv')
#         for index, row in df.iterrows():
#             print(row.keywords)
#         # print(df.to_string())
#     print('end')



def getWordsFromTitle(text):
	keywords = pd.read_csv('keywords.csv')
	
	for index, row in df.iterrows():
             print(row.keywords)
             print(row.associated)
             print(row.action)
	
	return 'teste'


#to test:
text = 'bell pepper in the table of the dinner with food and rice and plant'
compoundWordsFinded = getWordsFromTitle(text)
print('end')
