import mysql.connector
import tweepy
import os

consumer_key = os.environ['TW_CONSUMER_KEY']
consumer_secret = os.environ['TW_CONSUMER_SECRET']
access_token = os.environ['TW_ACCESS_TOKEN']
access_token_secret = os.environ['TW_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = api.search('#ウマ娘')
num = 1 #ツイート数を計算するための変数
for tweet in tweets:
    print('twid : ', tweet.id)               # tweetのID
    print('user : ', tweet.user.screen_name)  # ユーザー名
    print('date : ', tweet.created_at)      # 呟いた日時
    print(tweet.text)                  # ツイート内容
    print('favo : ', tweet.favorite_count)  # ツイートのいいね数
    print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
    print('ツイート数 : ', num) # ツイート数
    print('='*80) # =を80個表示
    num += 1 # ツイート数を計算
    if num > 3:
        exit;

#db = mysql.connector.connect(
#    host='172.19.0.2',
#    port='3306',
#    user='root',
#    password='root',
#    database='test_database'
#)
#cursor=db.cursor()

#query = "SELECT * FROM test"
#cursor.execute(query)
#print(cursor.fetchall())
