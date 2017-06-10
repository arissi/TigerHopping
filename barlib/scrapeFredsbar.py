import json
import requests
import re

def scrapeFredsbar():
    try:
        # fred's provides an api for their events
        response = requests.get('https://inffuse-calendar2.appspot.com/api/events?calendar=fredsintigerland@gmail.com&count=50&from=1487930400000&project=proj_IsvT8dAxN5GIU2QtLbtkS&user=user_Va2QnKo7EC0cl1POd4oC3')
        jsonData = json.loads(response.text)
        # pull all the event titles from json
        titles = [x['title'] for x in jsonData['events']]

        # use regex(words until 'T' or Blank) to pull all the event dates from json
        dateRegex = re.compile(r'.+?(?=T|$)')
        dates = []
        for event in jsonData['events']:
            date = dateRegex.search(event['start_time'])
            if date:
                dates.append(date.group())
            else:
                dates.append('None')

        # pair each special with its corresponding day using zip 
        # convert list of tuples to a dictionary and return in JSON format
        return json.dumps([dict(zip(dates, titles))])
    except requests.exceptions.RequestException as e:
        print('Error making Fred request: {}'.format(e))