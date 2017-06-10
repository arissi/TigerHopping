import bs4 as bs
import requests
import datetime
import json

def scrapeBogiesBR():
    try:
        source = requests.get('http://www.bogiesbr.com/').text
        soup = bs.BeautifulSoup(source, 'lxml')

        # scrape specials and days from website using css selectors
        days = soup.select('div.grid_3 h2')
        specials = soup.select('div.grid_3 h3')

        # Take todays date. Subtract the number of days which already passed this week to get last monday
        today = datetime.date.today()
        last_monday = today - datetime.timedelta(days=today.weekday())

        # Create a range of dates from Monday until Saturday
        # save dates as a string using strftime
        numDays = 6
        dateList = [(last_monday + datetime.timedelta(days=x)).strftime('%Y-%m-%d') for x in range(0, numDays)]
        # save a list of weekdays too
        weekdayList = [(last_monday + datetime.timedelta(days=x)).strftime('%A') for x in range(0, numDays)]


        # compare days with for 3 letters of weekdayList. if they don't match, use index to insert a 'None'
        # placeholder in the specials list so that the dates match up correctly
        for index, day in enumerate(weekdayList):
            if (day[:3] != days[index].text):
                days.insert(index, 'None')
                specials.insert(index, 'None')
            else:
                specials[index] = specials[index].text

        # pair each special with its corresponding day using zip 
        # convert list of tuples to a dictionary and return in JSON format
        return json.dumps([dict(zip(dateList, specials))])
        
    except requests.exceptions.RequestException as e:
        print('Error making Bogie\'s request: {}'.format(e))