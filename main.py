import tweepy as tw
import pandas as pd


# Function to extract tweets
def get_tweets(username):

    api_key = ""
    api_key_secret = ""

    access_token = ""
    access_token_secret = ""

    auth = tw.OAuthHandler(api_key, api_key_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_token, access_token_secret)

    # Calling api
    api = tw.API(auth, wait_on_rate_limit=True)

    # number tweets to be extracted
    number_of_tweets = 200
    tweets = api.user_timeline(screen_name=username)

    # pandas bs incoming
    columns = ['Time', 'User', 'Tweet']

    # Empty Array
    tmp = []

    # create array of tweet information: username,
    # time, user, text
    for tweet in tweets:
        # Appending tweets to the empty array tmp
        tmp.append([tweet.created_at, tweet.user.screen_name, tweet.text])

        # data stored in tmp to csv file using pandas
        df = pd.DataFrame(tmp, columns=columns)
        # Printing the tweets
        df.to_csv('tweets.csv')

        print(df)


# Driver code
if __name__ == '__main__':
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("")
