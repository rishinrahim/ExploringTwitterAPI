from bs4 import BeautifulSoup
import tweepy

class TwitterAPI:
    
    def __init__(self, api_key, api_secret, access_token,access_token_secret):
        self.api_key = api_key
        self.api_secret = api_secret 
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        
    
    def create_api(self):

        auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        return api
    
    


    

