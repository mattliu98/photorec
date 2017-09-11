import praw
import pprint
import requests
import urllib.request as u
import re
import collections
import json
#auth info:
reddit = praw.Reddit(client_id='FwTAWNvo0KMYAw',
                     client_secret='pTMohyBCYCLlRbshZkBuZMpF0ps',
                     password='matt82186',
                     user_agent='photorec by /u/appdev5',
                     username='appdev5')

def makehash():
    return collections.defaultdict(makehash)
def findDim(title):
    try:
        parse = re.search("(\[|\()[0-9]{4,5}.+[0-9]{3,4}", title)
        length = parse.group(0)[1:5]
        reparse = re.search("[0-9]{3,4}", parse.group(0)[5:])
        width = reparse.group(0)
        return length, width
    except AttributeError:
        print("wrong dimensions")
def saveImage(suburl):
    if (suburl[:16] == "http://imgur.com"):
        url = "http://i.imgur.com" + suburl[16:] + ".jpg"
    else:
        url = suburl
    try:
        u.urlretrieve(url, "img/" + submission.id + ".jpg")
        l, w = findDim(submission.title)
        img[submission.id]["length"] = l
        img[submission.id]["width"] = w
        img[submission.id]["name"] = submission.title
        img[submission.id]["score"] = submission.score
    except Exception:
        print("this url doesn't work properly")

img = makehash()
subreddit = reddit.subreddit("EarthPorn")
for submission in subreddit.top(limit=5):
    toprint = "{} , score={}".format(submission.title, submission.score)
    print(submission.url)
    print(toprint)
    saveImage(submission.url)
with open('imgs.json', 'w') as f:
     json.dump(img, f)

# pprint.pprint(vars(post))
