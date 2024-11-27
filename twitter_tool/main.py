import tweepy

consumer_key = f'SxLx82LbesGYZb0tD1x2lipsA''
consumer_secret = f'cPDKaOjp5g1jlECg4pJnMGPqOCJXfuHl2bEuSordMz7Dnt9DUj'
access_token = f'1740673965813620736-wZIXmxePrEKuNH8UU2yPs7nxzrb3RV'
access_token_secret = f'NMsEXPNA2ugnLjPcr1ONwqya1F2DpKGPuDalvHmDO3kHF'

# Authorization and Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def main():
    