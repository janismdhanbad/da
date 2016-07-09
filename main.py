
from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()
entities = {}
mytext = open('mytext.txt','r')
mytext = mytext.read()


response1 = alchemyapi.entities("text",mytext)
response = alchemyapi.keywords("text",mytext)
response3 = alchemyapi.relations("text",mytext)


en1 = response1['entities'][0]['text']
en2 = response1['entities'][1]['text']

key1 = response['keywords'][0]['text']
key2 = response['keywords'][1]['text']
key3 = response['keywords'][2]['text']
key4 = response['keywords'][3]['text']
key5 = response['keywords'][4]['text']
key6 = response['keywords'][5]['text']





