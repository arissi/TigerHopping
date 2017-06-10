import bs4 as bs
import requests
import datetime
import json

def scrapeJLsPlaceBR():
    try:
        # page rejects GET requests that do not identify a User-Agent
        headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        source = requests.get('https://digbr.com/jls-place/', headers=headers).text
        soup = bs.BeautifulSoup(source, 'lxml')

        # scrape specials from website using css selectors
        divs = soup.select('div.ult-new-ib-content p')

        # separate the text from the divs and replace new line
        specials = [div.text.replace('\n', ' ') for div in divs]

        # DIGBR LINK IS BROKEN. USE PLACEHOLDER FOR NOW
        specials = ['NONE', 'Free drinks 8-10', 'NONE', 'Penny pitchers 8-10, Free cover for girls 10-12, Free cover for Greeks 10-11', 'Free drinks 8-10', 'Open bar 8-10']

        # Take todays date. Subtract the number of days which already passed this week to get last monday
        today = datetime.date.today()
        last_monday = today - datetime.timedelta(days=today.weekday())

        # Create a range of dates from Monday until Saturday
        # save dates as a string using strftime
        numDays = 6
        dateList = [(last_monday + datetime.timedelta(days=x)).strftime('%Y-%m-%d') for x in range(0, numDays)]

        # pair each special with its corresponding day using zip 
        # convert list of tuples to a dictionary and return in JSON format
        return json.dumps([dict(zip(dateList, specials))])
    except requests.exceptions.RequestException as e:
        print('Error making JL\'s request: {}'.format(e))