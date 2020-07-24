from apscheduler.schedulers.blocking import BlockingScheduler
import twitter_bot

#first call twit-bot once
twitter_bot.main()

#creating a time scheduler to run code every two hours
scheduler = BlockingScheduler()
scheduler.add_job(twitter_bot.main, 'interval', hours=2)
scheduler.start()
