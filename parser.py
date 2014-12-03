from os import path, makedirs
from urllib2 import urlopen
from bs4 import BeautifulSoup as bs
from urlparse import urljoin, urlsplit


url = raw_input()
if url[:7] != 'http://' and url[:8] != 'https://':
        url = 'http://'+url
page = urlopen(url).read()
soup = bs(page)

for link in soup.find_all('a'):
    if link.get('href')[-4:] == '.pdf':
        down = urljoin(url, link.get('href'))
        split = urlsplit(down)
        filename = split.path.split("/")[-1]
        f = urlopen(down)
        data = f.read()
        if not path.exists("out"):
            makedirs("out")
        with open("out/"+filename, "wb") as code:
            code.write(data)
            print "Downloaded " + filename