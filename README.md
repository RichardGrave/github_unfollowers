# The Github unfollowers
## Keeping track of github unfollowers

It's always awesome if you get new followers on Github.\
But not all followers are **real** followers.\
By that I mean the followers that if you follow them back,\
they unfollow you within a couple of days (some a couple of weeks later).\
Sometimes even the same day you follow them back.

At first I couldn't figure out why people would do that.\
Then I read somewhere on the internet (not sure if this is really true)\
that people try to get lots of followers by following them.\
They wait till those people follow them back so they can unfollow them.\
Trying to create the illusion that they are somebody important.\
Somebody that many people want to follow.

Because it looks way cooler if you have\
**900 followers and following 10**\
than\
**10 followers and following 900**

When I read that, I thought that was a bit far fetched.\
But then a few weeks later it happend again.\
Somebody unfollowed me after I started following that user.\
I looked on that users profile every day for more than a week.\
Apparently he/she started following lots and lots of people and later on removing them.\
Probably using a script or something (like this project)\
Watching the number of followers slowly rise and the following going up and down every now and then.

So I unfollowed that github user to see what would happen.\
Then a couple of days later that person was following me again.\
I was curious of what would happen if I didn't follow back.\
Waited for more than a week. Nothing happend.\
Then I followed the github user again and the same day that person unfollowed me again.

## The idea
That gave me the idea to find the profiles that unfollow me.\
I came up with this idea more than a year ago,\
but I always had other things I wanted to created first (also to learn more Rust).\
I had almost forgotten about this idea and decided not to postpone it any longer.

So I wanted to keep a file with followers and when I have less followers\
to find the users that are in the file but are not following on github anymore.\
Writing them to an unfollowers file that can be used to unfollow them.

I didn't want one script to do it all.
So I have one script to collect the unfollowers and append them to a unfollowers file.\
And another script to use that file to unfollow them.
Then at least I can decide when to unfollow.

Just keep in mind that it always needs a file with your current followers.

The first time the find script is executed it only creates a followers file (filename is the given github name).
If the file exists then every time when the find script is executed,\
it will overwrite the followers file with your current followers.
And append unfollowers (if found) in the unfollower file.

If the unfollow script is executed it will unfollow everyone that is in the file\
and also empty the file.

## Use at your own risk
**I created these scripts for myself.**\
If you want to use them, then **use the scripts at your own risk.**\
The scripts seem to work fine for me, but **if** I've made a mistake somewhere\
then it's no fun if you suddenly unfollow the wrong people.

Therefore again, **use the scripts at your own risk.**

If you want to use the scripts then you'll need a 
[Personal Access Token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) for your own github profile.

The script is looking for a file with the name 'github_pat.txt'\
in the same dir or one dir above.
That ofcourse contains the Personal Access Token.

If you copy this project then **NEVER** commit your token.
I use an .ignore file that excludes the '.txt' files,\
but **ALWAYS** be carefull when commiting files.
You don't want anyone to use your token and mess up your github profile.

You can run the find_followers script like this:\
**python3 find_unfollowers.py user=your_github_name_here**

Then for the unfollowing:\
**python3 unfollow_them.py user=your_github_name_here**

## Third-party library
I have used the [PyGithub](https://github.com/PyGithub/PyGithub) library.\
That can be found on the Github page [Libraries](https://docs.github.com/en/rest/overview/libraries) among lots of other libraries.\
There are also libraries for many different programming languages.

