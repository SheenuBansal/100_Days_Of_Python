# HTTPError – It is raised for the exotic HTTP errors, such as the authentication request errors. 
# It is a subclass or URLError. Typical errors include ‘404’ (page not found), ‘403’ (request forbidden),
# and ‘401’ (authentication required).


import urllib.request
import urllib.parse
  
# trying to read the URL
try:
    x = urllib.request.urlopen('https://www.google.com / search?q = test')
    print(x.read())
  
# Catching the exception generated    
except Exception as e :
    print(str(e))
