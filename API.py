import urllib2
import json

def fullContactCollect(email):
	api_key = '6efaee0862de3d66'
	email = email
	fullURL = 'https://api.fullcontact.com/v2/person.json?email='+ email +'&apiKey='+ api_key +''
	loadUrl = urllib2.urlopen(fullURL)
	jsonData = json.load(loadUrl)

	print jsonData
	photos = jsonData['photos']
	profile = jsonData['socialProfiles']
	for items in profile: 
		print items
		print items['typeName'],items['url']
	
	
		

	for item in photos:
		print item['url']


fullContactCollect('example@gmail.com')

#urlData =  urllib2.urlopen(url)
#loadedJson = json.load(urlData)
#print loadedJson
#loadedJson['photos']

