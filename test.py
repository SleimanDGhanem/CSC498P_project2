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
        output = open("subdomains_output.bat", "w")
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

def returnDirectories(url):
    with open("dirs_dictionary.bat") as file:
        output = open("directories_output.bat", "w")
        for string in file:
            word = string.strip()
            result = url + "/" + word
            check_directories = request(result)
            if check_directories:
                output.write(result + "\n")
        output.close()

if test:
    returnDirectories(url)
else :
    print("url not found, please retry")	
    
