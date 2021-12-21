
from urllib.parse import *

# PARSING : Separates different components of URL
parse_url = urlparse('https://practice.geeksforgeeks.org/contest/job-a-thon-4-hiring-challenge')
print(parse_url)

parse_url_2 = urlparse('https://www.youtube.com/results?search_query=urllib+python+')
print(parse_url_2)

# UNPARSING : Join different components of URL
unparse_url = urlunparse(parse_url)
print(f"\n{unparse_url}")

# URLSPLIT : It is similar to urlparse() but doesn’t split the params
url_split = urlsplit("https://www.geeksforgeeks.org/args-kwargs-python/?ref=leftbar-rightbar")
print(url_split)

# URLDEFRAG : If URL contains fragment, then it returns a URL removing the fragment.
url_defrag = urldefrag("https://www.geeksforgeeks.org/args-kwargs-python/?ref=leftbar-rightbar")
print(url_defrag)
