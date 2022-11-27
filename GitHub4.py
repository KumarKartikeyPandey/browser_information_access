import urllib
import webbrowser
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
weburl=urllib.request.urlopen('http://www.geeksforgeeks.com/')
html=weburl.read()
data=weburl.getcode()
url=weburl.geturl()
hd=weburl.headers
inf=weburl.info()
print("The url is",url)
print("HTTP status code is",data)
print("the info() returned \n:",inf)
print("Now opening the url",url)
webbrowser.open_new(url)

