var Bar = require('./models/bar'),
    Rsvp = require('./models/rsvp'),
    User = require('./models/user');

var data = [ 
    {
        name: 'Freds'
    },
    {
        name: 'Reggies'
    },
    {
        name: 'Bogies'
    },
    {
        name: 'Mikes'
    },
    {
        name: 'JLs'
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