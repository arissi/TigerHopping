from apscheduler.schedulers.background import BackgroundScheduler
from os import system
from datetime import datetime
from time import sleep

# Edit global TWITTER_NAME for different bar
TWITTER_NAMES = ['ReggiesBR', 'Fredsbar', 'BogiesBR', 'MikesNTigerland', 'JLsPlaceBR', 'barcadiabr']
try:
    print('Attempting to get new tweets')
    for bar in TWITTER_NAMES:
        # Gather new tweet 
        print('Getting most current tweet for {} @ {}'.format(bar, datetime.now()))
        system('python getTweetFromBar.py ' + bar)
        print('Tweet collected @ {}'.format(datetime.now()))
except:
    print('Tweet Setup failed @ {}'.format(datetime.now()))
    print('Exiting barTweetScheduler.py')
    quit()

def updateTweets():
    try:
        for bar in TWITTER_NAMES:
            system('python getTweetFromBar.py ' + bar)
            print('Tweet updated @ {}'.format(datetime.now()))
    except:
        print('Tweet update failed @ {}'.format(datetime.now()))


tweetScheduler = BackgroundScheduler()
tweetScheduler.add_job(updateTweets, 'interval', minutes=30, id='updateTweets')
tweetScheduler.start()
while True:
    sleep(60)

