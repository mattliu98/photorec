import praw
import pprint
import requests
import urllib.request as u
import re
import collections
import json
from PIL import Image
#auth info:
reddit = praw.Reddit(client_id='FwTAWNvo0KMYAw',
                     client_secret='pTMohyBCYCLlRbshZkBuZMpF0ps',
                     password='matt82186',
                     user_agent='photorec by /u/appdev5',
                     username='appdev5')

print("hi")
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
    if (suburl[:18] == "http://i.imgur.com" or suburl[:19] == "https://i.imgur.com"
    or suburl[:14] == "https://i.redd"):
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
def processImages():
    res = (1920, 1080)
    with open("imgs.json", 'r') as json_data:
        data = json.load(json_data)
    images = list(data.keys())
    print("images" + str(images))
    for img in images:
        # if int(data[img]["length"]) > 1000 and int(data[img]["width"]) > 540:
        currentImage = Image.open("img/" + img + ".jpg")
        print(currentImage.size)
        resizedImage = currentImage.resize(res)
        data[img]["length"] = 1920
        data[img]["width"] = 1080
        with open('imgs.json', 'w') as f:
             json.dump(data, f)
        resizedImage.save("img/" + img + ".jpg")
        print(currentImage.size)
        print(resizedImage.size)
img = makehash()
subreddit = reddit.subreddit("EarthPorn")
for submission in subreddit.top(limit=50):
    toprint = "{} , score={}".format(submission.title, submission.score)
    print(submission.url)
    print(toprint)
    saveImage(submission.url)
with open('imgs.json', 'w') as f:
     json.dump(img, f)
print("processing")
processImages()
# pprint.pprint(vars(post))
