# URLError – It is raised for the errors in URLs, or errors while fetching the URL due to connectivity, 
# and has a ‘reason’ property that tells a user the reason of error.


import urllib.request
import urllib.parse
  
# trying to read the URL but with no internet connectivity
try:
    x = urllib.request.urlopen('https://www.google.com')
    print(x.read())

# Catching the exception generated     
except Exception as e :
    print(str(e))
