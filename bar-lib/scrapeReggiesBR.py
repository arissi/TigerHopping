import bs4 as bs
import requests
import datetime
import json

def scrapeReggiesBR():
    try:
        source = requests.get('http://reggiesbr.com/calendar').text
        soup = bs.BeautifulSoup(source, 'lxml')
        # scrape events from calendar
        specials = []
        days = soup.select('span.date')
        for day in days:
            special = day.parent.text
            special = ' '.join(special.split())
            # remove non-ascii text
            special = special.encode('ascii',errors='ignore')
            specials.append(special.decode('utf-8'))

        # Take todays date. Subtract the number of days which already passed this week to get last monday
        today = datetime.date.today()
        last_monday = today - datetime.timedelta(days=today.weekday())

        # Create a range of dates from Monday until Saturday
        # save dates as a string using strftime
        numDays = 6
        dateList = [(last_monday + datetime.timedelta(days=x)).strftime('%Y-%m-%d') for x in range(0, numDays)]

        # pair each special with its corresponding day using zip 
        # convert list of tuples to a dictionary and return in JSON format
        print(specials)
        return json.dumps([dict(zip(dateList, specials))])
    except requests.exceptions.RequestException as e:
        print('Error making Reggie\'s page request: {}'.format(e))
