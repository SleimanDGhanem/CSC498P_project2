import requests
import sys
import re

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
        for string in file:
            word = string.strip()
            result = word + "." + url
            response = request(result)
            if response:
                output.write(result + "\n")
        output.close()

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
 
def domainTest(domain, url):
    result = url.find(domain)
    if result != -1:
        return True
    else:
        return False   
def returnFiles(url):
    with open("files_output.bat", "a") as output:
        response = request(url)
        html = response.content.decode("utf-8")
        sites = re.findall('(?:href=")(.*?)"', html)
        for file in sites:

            test = request(file)
            if test:
                if test.status_code == 200:
                    checkDomain = domainTest(url, file)
                    if checkDomain:
                        returnFiles(file)
                    else:
                        continue
            else:
                try:
                    test = requests.get(file)
                    if not test:
                        website = url + "/" + file
                        output.write(site + "\n")
                except requests.exceptions.ConnectionError:
                    pass
                except requests.exceptions.InvalidURL:
                    pass
                except requests.exceptions.MissingSchema:
                    website = url + "/" + file
                    output.write(website + "\n")

url = sys.argv[1]
response = request(url)
if response:
    open("files_output.bat", "w").close()
    returnFiles(url)
else:
    print("url not found, please try again")
    sys.exit(0)
