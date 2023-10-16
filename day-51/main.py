import time
from internet_speed_twitter_bot import InternetSpeedTwitterBot

internet_bot = InternetSpeedTwitterBot()

internet_bot.get_internet_speed()
time.sleep(2)
internet_bot.tweet_at_provider()
