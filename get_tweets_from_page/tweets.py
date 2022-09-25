import tweepy
import json
from datetime import datetime
from datetime import timedelta

def main():
    bearer_token = "Your own tocken"

    client = tweepy.Client(bearer_token=bearer_token)

    response = client.search_recent_tweets(query="from:googleafrica -is:retweet", media_fields=['preview_image_url', 'url'], user_fields=['profile_image_url','verified'], tweet_fields=['created_at','lang'], expansions=['author_id','attachments.media_keys'])

    users = {u['id']: u for u in response.includes['users']}
    media = {m["media_key"]: m for m in response.includes['media']}

    tweets_json_arr = []

    for tweet in response.data:
        id = tweet.id
        text = tweet.text

        date = tweet.created_at

        username = None
        name = None
        profile_pic = None
        verified = False
        media_pic = None

        if users[tweet.author_id]:
            user = users[tweet.author_id]

            username = user.username
            name = user.name
            profile_pic = user.profile_image_url
            verified = user.verified

        try:
            media_keys = tweet.data['attachments']['media_keys']
            if media[media_keys[0]].url:
                media_pic = media[media_keys[0]].url
        except:
            pass

        tweet_obj = {
            "id": id,
            "name": name,
            "username" : username,
            "profilePic" : profile_pic,
            "verified": verified,

            "text": text,
            "date": date,
            "photo": media_pic
        }

        tweets_json_arr.append(tweet_obj)


    jsoned_tweets = json.dumps(tweets_json_arr)
    return jsoned_tweets



