
# TigerHopping Nightlife Tracker

I built this Nightlife Tracker application as a project for students in my local college. You can easily view the most up to date deals/events being offered by these bars and then indicate where you intend to go based off the information. Users must authenticate themselves through twitter to use the app's RSVP functionality.

### User stories:

* As an unauthenticated user, I can view popular bars in the tigerland area.
* As an unauthenticated user, I can view current deals/event happening in the tigerland area.
* As an authenticated user, I can add myself to a bar to indicate I am going there tonight.

# Web Scraper

The node app communicates with a Web Scraper to get information from the bars websites and update status

Responsible for:
* Accessing the Twitter API through Python
* Accessing and update the Mongo database
* Using an automated process to post twitter data to Database.

### Built using:

* Node.js
* Express.js
* Twitter's API
* MongoDB
* Python 2.7
* Python Libraries: BeautifulSoup, Tweepy

### Deployed

The app is deployed [here](https://tigerhopping.herokuapp.com/) at Heroku (also using [MongoLab](http://mlab.com)).

