import praw           #name folder diferent form the module imrted
reddit=praw.Reddit(client_id="BwCsGCoI2YV_tw",     #found after creating ap
                   client_secret="1qVSDq0r1OxurrOeaITb29UHfQfT0w",
                   username="funboi_007",
                   password="*_%5w6nB_qud5HH",
                   user_agent="Watermelon")#can be anything
                                

subreddit =reddit.subreddit("memes")#category
top = subreddit.top(limit = 5)#top posts

for submission in top:
    print(submission.title)
 