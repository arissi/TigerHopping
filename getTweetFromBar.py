#use command line to retrieve tweets
from sys import argv 
from api import getAPI
from twitter-config.database import configDB
import pymongo
from pymongo import MongoClient
import re
from datetime import datetime
from pytz import timezone
import json
import os
from bar-lib.scrapeReggiesBR import scrapeReggiesBR
from bar-lib.scrapeMikesNTigerland import scrapeMikesNTigerland
from bar-lib.scrapeBogiesBR import scrapeBogiesBR
from bar-lib.scrapeFredsbar import scrapeFredsbar
from bar-lib.scrapeJLsPlaceBR import scrapeJLsPlaceBR
from bar-lib.scrapebarcadiabr import scrapebarcadiabr

DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASS = configDB()

# database configuration
connection = MongoClient(DB_HOST, DB_PORT)
db = connection[DB_NAME]
db.authenticate(DB_USER, DB_PASS)

def main():

    functionMapping = {
        'ReggiesBR': scrapeReggiesBR,
        'MikesNTigerland' : scrapeMikesNTigerland,
        'BogiesBR' : scrapeBogiesBR,
        'Fredsbar' : scrapeFredsbar,
        'JLsPlaceBR' : scrapeJLsPlaceBR,
        'barcadiabr' : scrapebarcadiabr
    }

    try:
        arg = argv[1]
        api = getAPI()

        # get today's date and time
        today = datetime.today().strftime('%Y-%m-%d')
        central = timezone('US/Central')
        central_time = datetime.now(central)
        print central_time.strftime('%H')

        # store the special from the web scraper
        scrapeFunction = functionMapping[arg]
        data = json.loads(scrapeFunction())

        if today in data[0]:
            todaysSpecial = data[0][today]
        else:
            todaysSpecial = 'NONE'
        
        
        # make tweet better
        tweet = api.user_timeline(screen_name=arg, count=1)[0].text
        tweet = cleanTweet(tweet)

        # update tweet and special in db
        bars = db.bars
        rsvps = db.rsvps
        bar = bars.find_one({ 'username' : arg })
        if bar is not None:
            if central_time.strftime('%H') == 6:
                rsvps.remove({})
                bar['rsvps'] = []
            bar['tweet'] = tweet
            bar['special'] = todaysSpecial
            bars.save(bar)
    except IndexError:
        print("Program Missing Arg. Twitter Handle")
    except Exception as e:
        print (type(e))
        print (e.args)
        print ("Program Failure. Error: {}".format(e))

def cleanTweet(tweet):
    # regex to extract emojis from string
    emojiRegex = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    tweet = emojiRegex.sub(r'', tweet)

    # remove instances of single quotation marks
    if tweet.count('"') == 1:
        tweet.replace('"', '')
    # fix '&' character
    if 'amp;' in tweet:
        tweet.replace('amp;', '')
    
    return tweet


# code only executes when you want to run it as a program, not import
if __name__ == '__main__':
    main()