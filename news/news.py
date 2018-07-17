from newsapi import NewsApiClient
import sys
sys.path.insert(0,"../")
import config

API = NewsApiClient(api_key=config.NEWS_API_KEY)

def get_sources():
	return API.get_sources()
