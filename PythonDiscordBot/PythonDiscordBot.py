# bot.py
import os
import requests
import discord
import tweepy

from dotenv import load_dotenv

ckey = 'wiV1xCRRptUOBSSCnOJuskby4'
csecret = '7pMobiuKqSc4QqzPDEZFqXbv57gqfXFusPc4y3CYcz16quH1VD'
atoken = '1284634727778078720-2DuHfE54nvaz5UXOg2ZqJMZQ7kMzrM'
asecret = 'mIrLXuBnqOeQ8rsZWETM0IQNryLRe2pedsQmqxDV5KXDH'
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

tweets = api.home_timeline()
tweet = api.user_timeline(screen_name = 'realDonaldTrump', count = 1)[0]
print(tweet.text)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    await client.wait_until_ready()
    channel = client.get_channel(734179716738580521)
    guild = discord.utils.get(client.guilds, name='Team No Hetero')

    ##for guild in client.guilds:
    ##       for member in guild.members:
    ##            print(member) # or do whatever you wish with the member detail
 
@client.event                
async def on_message(message):
    await client.wait_until_ready()
    channel = client.get_channel(734179716738580521)
   ## if message.content == ('get.tweet'):
    r = requests.get('GET https://api.twitter.com/1.1/statuses/show.json?id=210462857140252672')
    print(r.text)
    
    



client.run(TOKEN)

