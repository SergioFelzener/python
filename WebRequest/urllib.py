import urllib.request, urllib.parse, urllib.error

response = urllib.request.urlopen("http://www.bancocn.com")
html = response.read()
print(html)
