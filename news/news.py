import const
from newsapi import NewsApiClient

import sys
sys.path.insert(0,"../")
import config

API = NewsApiClient(api_key=config.NEWS_API_KEY)

# returns live top/breaking headlines from the live sources only
def get_headline_news(keyphrase, sources, country, category):
	return API.get_top_headlines(q=keyphrase, sources=sources, language=config.DEFAULT_LANGUAGE, country=country, category=category)

# returns the subset of sources that live headline news is coming from
def get_headline_sources(category, country):
	return API.get_sources(category=category, language=config.DEFAULT_LANGUAGE, country=country)

# large search of millions of articles across ~5K sources
def get_historic_news(keyprhase, sources, domains, fromDateStr, toDateStr, ordering):
	return API.get_everything(q=keyphrase, sources=sources, domains=domains, from_param=fromDateStr, to_param=toDateStr, language=config.DEFAULT_LANGUAGE, sort_by=ordering, country=country)
