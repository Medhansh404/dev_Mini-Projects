import requests
import os
import json
from dotenv import load_dotenv
from requests_oauthlib import OAuth1

API_key = f'SxLx82LbesGYZb0tD1x2lipsA'
API_Secret_key = f'cPDKaOjp5g1jlECg4pJnMGPqOCJXfuHl2bEuSordMz7Dnt9DUj'
bearer_token = f"AAAAAAAAAAAAAAAAAAAAAFTDrgEAAAAAkOMngNmsKNl%2FPJgk0AstyTm64xI%3DdLvj0Qiwt1x7g8tMCU2lD2hzsWuEUQJIvlCbGRnYEfJJuxq9MF"
Access_Token = '1740673965813620736-wZIXmxePrEKuNH8UU2yPs7nxzrb3RV'
Access_Token_secret = 'NMsEXPNA2ugnLjPcr1ONwqya1F2DpKGPuDalvHmDO3kHF'

auth = OAuth1(API_key, API_Secret_key, Access_Token, Access_Token_secret)

print(bearer_token)
search_url = "https://api.twitter.com/2/tweets/search/recent"

query_params = {'query': '(from:twitterdev -is:retweet) OR #twitterdev', 'tweet.fields': 'author_id'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dump(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()

'''
def create_post():
    post_content =
    

def edit_post():
    content_edit =

def make_post():


def create_queue(mssg_id, ):


def authenticate():
'''
