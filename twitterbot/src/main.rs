use std::env;

fn main() {
    println!("Hello, world!");

    // What will the bot do?
    // The bot will read mentions to @sorenroodbot and respond to them.
    // First we have to come up with a way to handle new messages.
    // I'll start by posting something to twitter using rust.
    let consumer_key = env::var_os("twitter_consumer_key");
    let consumer_secret = env::var_os("twitter_consumer_secret");
    let con_token = egg_mode::KeyPair::new("something", "something"); // doesn't work yet





}
