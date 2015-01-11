#import urllib2
#response = urllib2.urlopen('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
#response = urllib2.urlopen('https://hacker-news.firebaseio.com/v0/item/8648280.json?print=pretty')
#print response.read()
#for story in top_story_ids:
#   print hn.get_item(story)

from hackernews import HackerNews
hn = HackerNews()
top_story_ids = hn.top_stories()
#for story in top_story_ids:
#	print hn.get_item(story)
for story_id in hn.top_stories(limit=10):
    print hn.get_item(story_id)