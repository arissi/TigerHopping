var Bar = require("../models/bar"),
    Rsvp = require("../models/rsvp"),
    middleware = require("../middleware");

module.exports = function(app, passport) {

// INDEX - show all bars
app.get("/", function(req, res) {
    Bar.find({}, function(err, foundBars) {
        if (err) {
            console.log(err);
        } else {
            res.render("index", {bars: foundBars, currentUser: req.user});
        }
    });
});

// SHOW - show the login form
// app.get("/login", function(req, res) {
//     res.render("login");
// });


// CREATE - create a new comment, then redirect to the specific campground
app.post("/:id/rsvp", middleware.isLoggedIn, function(req, res) {
    Bar.findById(req.params.id, function(err, foundBar) {
        if (err) {
            console.log(err);
            res.redirect("/");
        } else {
            Rsvp.create({}, function(err, rsvp) {
                if (err) {
                    console.log(err);
                } else {
                    rsvp.author.id = req.user._id;
                    rsvp.author.username = req.user.twitter.username;
                    rsvp.save();
                    foundBar.rsvps.push(rsvp);
                    foundBar.save();
                    req.flash("success", "RSVP added");
                    res.redirect("/");
                }
            });
        }
    });
});

// Twitter authentication routes
app.get('/auth/twitter', passport.authenticate('twitter'));
app.get('/auth/twitter/callback',
  passport.authenticate('twitter', { successRedirect: '/',
                                     failureRedirect: '/' }));

};
