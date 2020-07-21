import tweepy
import requests
import random
import time
import goodreads

consumer_key = 'JKJajqHdI4bKiih5xH16VBKal'
consumer_secret = 'FD7UgwNlx4lCJTvLzmEjES4TsDAA5vTtsvQN3hpZoB7h9Ohsjt'
access_token = '1079243430038028288-shSBTbf57mgg0YDXrVuTjAla26Fz3Q'
access_token_secret = 'cWmD8ySydu05JhYIkg2yfHPBRXd7xE6jfQmq8DE3r39BZ'
#quotes_url = 'https://type.fit/api/quotes'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def find_quote():
    #request = requests.get(quotes_url)
    #r_json = request.json()
    #quote = random.choice(r_json)
    quote = goodreads.main()
    return quote

def tweet(api, quote):
    #text = quote["text"] 
    #author = quote["author"]
    #if author == None:
    #    author = "Anonymous"

    #tweet = f'\"{text}\" \n{author}'
    tweet = quote
    api.update_status(tweet)

def main():
    print("Finding quote...")
    quote = find_quote()

    print("Setting up tweet...")
    tweet(api, quote)
    print("Tweeted!")
    

if __name__ == '__main__':
    #tweets once an hour
    while True:
        main()
        time.sleep(7200)
