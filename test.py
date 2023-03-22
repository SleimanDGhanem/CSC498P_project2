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
        
url = sys.argv[1]
print("the website you are searching through is " + url)
test = request(url)

if test:
    getSubdomains(url)
else :
    print("invalid url!")	