import praw
import pprint
import re
#auth info:
reddit = praw.Reddit(client_id='FwTAWNvo0KMYAw',
                     client_secret='pTMohyBCYCLlRbshZkBuZMpF0ps',
                     password='matt82186',
                     user_agent='photorec by /u/appdev5',
                     username='appdev5')


# subreddit = reddit.subreddit("leagueoflegends")
# for submission in subreddit.top(limit=10):
#     # toprint = "{} , score={}".format(submission.title, submission.score)
#     # print(toprint)
#     post = submission
# post = reddit.submission(id="6do239")
# print(post.score)
def findDim(title):
    try:
        parse = re.search("(\[|\()[0-9]{4,5}.+[0-9]{3,4}", title)
        length = parse.group(0)[1:5]
        reparse = re.search("[0-9]{3,4}", parse.group(0)[5:])
        width = reparse.group(0)
        print(length, width)
    except AttributeError:
        print("wrong dimensions")
findDim("Iowa, not just corn fields it turns out. [3200x2076] (OC)")
findDim("USA's Zion National Park in Utah on the hike up to Angels Landing. (OC) [3008*2000]")
findDim("Standing on the bank next to Dettifoss, Europe's mightiest waterfall. Iceland, 2014 [2048x1366 OC]")
findDim("The PNW is a magical place. OC [32432x2448]")
