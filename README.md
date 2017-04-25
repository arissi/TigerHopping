
# TigerHopping Nightlife Tracker

I built this Nightlife Tracker application as a project for students in my local college. You can easily view the most up to date deals/events being offered by these bars and then indicate where you intend to go based off the information. Users must authenticate themselves through twitter to use the app's RSVP functionality.


### User stories:

* As an unauthenticated user, I can view popular bars in the tigerland area.
* As an unauthenticated user, I can view current deals/event happening in the tigerland area.
* As an authenticated user, I can add myself to a bar to indicate I am going there tonight.

### Object-oriented modeling

* [Analysis Model](https://github.com/arissi/TigerHopping/blob/master/AnalysisModel.pdf)
* [Design Model](https://github.com/arissi/TigerHopping/blob/master/Design%20Model%20.pdf) 

### Built using:

* Node.js
* Express.js
* Twitter's API
* MongoDB

### Notes
* This app communicates with the Tigerland Web Scraper to scrape information from the bars websites and update the twitter status

### TODO
* User should onle be able to RSVP once
* RSVP count should reset every 24hrs
* Make fonts look better

### Deployed

The app is deployed [here](https://tigerhopping.herokuapp.com/) at Heroku (also using [MongoLab](http://mlab.com)).

