var mongoose = require("mongoose");

var barSchema = mongoose.Schema({
    name: String,
    username: String,
    tweet: String,
    special: String,
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