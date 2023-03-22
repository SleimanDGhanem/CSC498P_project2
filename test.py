import requests
import sys

def request(url):
  try:
    return requests.get("http://" + url)
  except requests.exceptions.ConnectionError:
    try: 
      return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
      pass
    

