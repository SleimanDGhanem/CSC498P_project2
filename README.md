# CSC498P_project2



####  The offered Python code is a script that searches a specified URL for subdomains, folders, and files to perform website enumeration. It makes use of the re library to parse HTML code, the requests library to submit HTTP requests to the website, and the sys library to retrieve the command-line arguments.
## Function 1: request
####  the first function, request, begins by defining the request function, which accepts a URL as an argument. To handle different protocols, the function tries to submit an HTTP GET request to the URL using both http:// and https:// prefixes. The request tries the other protocol if it encounters a connection error. It doesn't return anything if either request fails.

## function 2: getSubDomains
####  The next function is getSubdomains, which accepts a URL as an argument and searches subdomains by combining the URL with each word in the subdomains dictionary.bat file. For each subdomain, the script sends a request using the request function and writes the result to a file named "subdomains_output.bat" if the response is successful.
## Function 3: returnDirectories
####  The returnDirectories function accepts a URL as an argument and does a directory search using the URL together with each word from the "dirs_dictionary.bat" file. For each directory, the script sends a request using the request function and writes the result to a file named "directories_output.bat" if the response is successful.
## Function 4: domainTest
####  A domain and a URL are the two arguments for the domainTest function. If the domain is found in the URL, it returns True; if not, it returns False. this is used in the coming returnFiles function to test for valid domains
## Function 5: returnFiles
####  The returnFiles function accepts a URL as an input and uses that URL to send an HTTP request, parse the HTML content to extract links, and then look for files there. The script uses the request function to send a request to each link, then it checks to see if the response status code is 200. If so, the domainTest function of the script is used to see if the link is a member of the same domain as the URL. If so, the script repeatedly invokes the link's returnFiles function. The script skips the link if it doesn't. The script writes the URL to a file called files output.bat in the event that the link cannot be reached or throws an exception.

####  The main portion of the script uses the sys.argv function to accept a URL as a command-line parameter and then runs the request function to determine whether the Site is reachable. If so, the script calls the returnFiles function on the URL and deletes the files output.bat file. The script prints an error message and ends if it isn't.

## Problems Encountered
#### two problems encountered by me were singificantly slow performance, and the exception handling highly halted performance 