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


def getSubdomains(url):
    with open("subdomains_dictionary.bat") as file:
        output = open("subdomins_output.bat", "w")
        for line in file:
            word = line.strip()
            target = word + "." + url
            response = request(target)
            if response:
                print(target)
                output.write(target + "\n")
        output.close()
        
