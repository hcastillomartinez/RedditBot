import praw
import config

reddit = praw.Reddit(
    username=config.USERNAME,
    password=config.PASSWORD,
    client_id=config.CLIENT_ID,
    client_secret=config.CLIENT_SECRET,
    user_agent=config.USER_AGENT,
)

print(reddit.read_only)
