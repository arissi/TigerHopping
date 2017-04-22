var mongoose = require("mongoose");

var barSchema = mongoose.Schema({
    name: String,
    username: String,
    tweet: String,
    special: String,
    facebook: String,
    instagram: String,
    twitter: String,
    phone: String,
    image: String,
    banner: String,
    website: String,
    author: {
        id: {
            type: mongoose.Schema.Types.ObjectId,
            ref: "User"
        },
        username: String
    },
    rsvps: [{
        type: mongoose.Schema.Types.ObjectId,
        ref: "Rsvp"
    }]
});

module.exports = mongoose.model("Bar", barSchema);