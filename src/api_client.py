import pandas as pd
import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_articles(query,start=None,end=None):
    base_url = "https://newsapi.org/v2/everything?"
    q = query 
    relevancy = "popularity"
    apiKey = NEWS_API_KEY
    headers = {
        'User-Agent': 'curl/7.81.0'
    }
    if start and end:
        url = f"{base_url}q={q}&from={start}&to={end}&sortBy={relevancy}&apiKey={apiKey}"
    else:
        url = f"{base_url}q={q}&sortBy={relevancy}&apiKey={apiKey}"

    try:
        response = requests.get(url,headers=headers)
        response.raise_for_status()
        payload = response.json()
        return pd.json_normalize(payload,"articles",sep=".")
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return pd.DataFrame()














