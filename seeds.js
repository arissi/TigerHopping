var Bar = require('./models/bar'),
    Rsvp = require('./models/rsvp'),
    User = require('./models/user');

var data = [ 
    {
        name: 'Freds',
        username: 'Fredsbar',
        tweet: 'this is a tweet',
        special: 'this is a special',
        facebook: 'https://www.facebook.com/Fredsbar/',
        instagram: 'https://www.instagram.com/fredsbar/',
        twitter: 'https://twitter.com/fredsbar',
        phone: 'tel:2257663909',
        image: "img/Fred's.png",
        website: 'http://www.fredsintigerland.com/'
    },
    {
        name: 'Reggies',
        username: 'ReggiesBR',
        tweet: 'this is a tweet',
        special: 'this is a special',
        facebook: 'https://www.facebook.com/ReggiesBR/?rf=154414251274452',
        instagram: 'https://www.instagram.com/reggiesbr/',
        twitter: 'https://twitter.com/ReggiesBR',
        phone: 'tel:2257579555',
        image: "img/Reggie's.jpg",
        website: 'http://reggiesbr.com/'
    },
    {
        name: 'Bogies',
        username: 'BogiesBR',
        tweet: 'this is a tweet',
        special: 'this is a special',
        facebook: 'https://www.facebook.com/bogiesbr/?rf=133405190045306',
        instagram: 'https://www.instagram.com/bogies_br/',
        twitter: 'https://twitter.com/BogiesBR',
        phone: 'tel:2257664241',
        image: 'img/Bogie.jpg',
        website: 'http://www.bogiesbr.com/'
    },
    {
        name: 'Mikes',
        username: 'MikesNTigerland',
        tweet: 'this is a tweet',
        special: 'this is a special',
        facebook: 'https://www.facebook.com/Mikes-Daiquiris-Grill-126797682836/',
        instagram: 'https://www.instagram.com/mikesintigerland/',
        twitter: 'https://twitter.com/MikesNTigerland',
        phone: 'tel:2254482524',
        image: "img/Mike's.jpg",
        website: 'https://twitter.com/MikesNTigerland'
    },
    {
        name: 'JLs',
        username: 'JLsPlaceBR',
        tweet: 'this is a tweet',
        special: 'this is a special',
        facebook: 'https://www.facebook.com/JLs-Place-92259608830/',
        instagram: 'https://www.instagram.com/jlsplacebr/',
        twitter: 'https://twitter.com/JLsPlaceBR',
        phone: 'tel:2257657557',
        image: "img/JL's.jpg",
        website: 'https://www.facebook.com/JLs-Place-92259608830/'
    },
    {
        name: 'Barcadia',
        username: 'barcadiabr',
        tweet: 'this is a tweet',
        special: 'this is a special',
        facebook: 'https://www.facebook.com/BarcadiaBatonRouge/',
        instagram: 'https://www.instagram.com/barcadiabr/?hl=en',
        twitter: 'https://twitter.com/barcadiabr',
        phone: '2252246000',
        image: "img/barcadia.png",
        website: 'http://barcadiabars.com/barcadia-baton-rouge/'
    }
];

function seedDB() {
    // Remove all users
    User.remove({}, function(err) {
        if (err) {
            console.log('Error removing all users' + err);
        } else {
            console.log('Removed all users from the db.');
        }
    });
    
    // Remove all bars
    Bar.remove({}, function(err) {
        if (err) {
            console.log('Error removing all bars' + err);
        }
        console.log('Removed all bars from the db.');
        
        // add a few bars
        data.forEach(function(seed) {
            Bar.create(seed, function(err, newBar){
                if(err){
                    console.log('Error creating seed: ' + err);
                } else {
                    console.log("Added seed to the db");
                    // //create a rsvp
                    // Rsvp.create(
                    //     {
                    //         author: "Anthony"
                    //     }, function(err, newRsvp){
                    //         if(err){
                    //             console.log('Error seeding Rsvp' + err);
                    //         } else {
                    //             newBar.rsvps.push(newRsvp);
                    //             newBar.save();
                    //             console.log("Created new Rsvp seed");
                    //         }
                    //     });
                }
            });
        });
    });
}

module.exports = seedDB;