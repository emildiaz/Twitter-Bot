from apscheduler.schedulers.blocking import BlockingScheduler
import twitter_bot

#creating a time scheduler to run code every two hours
scheduler = BlockingScheduler()
scheduler.add_job(twitter_bot.main, 'interval', minutes=120)
scheduler.start()
