from __future__ import unicode_literals
import json, setting
from requests_oauthlib import OAuth1Session
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def final():
        if request.method == "GET":
            return render_template("final.html")

@app.route('/final-first', methods=["GET","POST"])
def final_first():
        if request.method == "GET":
            return render_template("final-first.html")

@app.route('/second', methods=["GET","POST"])
def second():
        if request.method == "GET":
            return render_template("second.html")



@app.route("/index", methods=["GET","POST"])
def search():

    CK = setting.CK
    CS = setting.CS
    AT = setting.AT
    ATS = setting.ATS
    twitter = OAuth1Session(CK, CS, AT, ATS)

    url = "https://api.twitter.com/1.1/search/tweets.json"
    # params = {"q" : keyword, 'count' : 5}
    # req = twitter.get(url, params = params)


    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        if "search" in request.form.keys():
            keyword = request.form["search"]
            params = {"q" : keyword, 'count' : 10}
            req = twitter.get(url, params = params)
            if req.status_code == 200:
                search_timeline = json.loads(req.text)
                # for tweet in search_timeline['statuses']:
                    # print(tweet['user']['name'] + '::' + tweet['text'])
                    # print(tweet['created_at'])
                    # print('------------------------------')
            # else:
            #     print("ERROR: %d" % req.status_code)
            return render_template("index.html", keyword=keyword, search_timeline = search_timeline)

if __name__ == '__main__':
    
    app.run(debug = True)