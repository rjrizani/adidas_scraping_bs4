from curl_cffi import requests
from bs4 import BeautifulSoup

def get_soap(url:str) -> dict:
    response = requests.get(url, impersonate= "chrome")
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}")
    return response.json()