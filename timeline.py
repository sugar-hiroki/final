import json, config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = ACCESS_TOKEN
ATS = ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

params ={'count' : 5}
req = twitter.get(url, params = paramas)

if req.status_code == 200:
    timeline = json.loads(req.text)
    for tweet in timeline:
        print(tweet['user']['name']+'::'+tweet['text'])
        print(tweet['created_at'])
        print('--------------------------------------')
else:
    print("ERROR : %d" % req.status_code)