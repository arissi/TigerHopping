import bs4 as bs
import requests
import datetime
import json

def scrapebarcadiabr():
    try:
        source = requests.get('http://barcadiabars.com/barcadia-baton-rouge/').text
        soup = bs.BeautifulSoup(source, 'lxml')
        # scrape events from calendar
        specials = []
        days = soup.select('#text-12 > div > span')
        for i in range(1, len(days)-1):
            nextone = days[i].nextSibling
            s = ''
            while nextone.name != 'span':
                while nextone.name == 'br':
                    nextone = nextone.nextSibling
                s += nextone
                nextone = nextone.nextSibling
            s = s.replace("\n", ' ')
            specials.append(s.encode('utf-8'))

        print(specials)
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
        print('Error making barcadia page request: {}'.format(e))

if __name__ == '__main__':
    scrapebarcadiabr()