from os import path, makedirs
from urllib2 import urlopen
from bs4 import BeautifulSoup as bs
from urlparse import urljoin, urlsplit


print "Please, write the URL where you want to download from"
url = raw_input()
print "What kind of file you wanna download? (type extension without the '.')"
filetype = raw_input()
print "Where do you wanna store the files? (write a relative path from where you are running this script, default is out/)"
outpath = raw_input()
if not outpath:
    outpath = "out/"

if url[:7] != 'http://' and url[:8] != 'https://':
        url = 'http://'+url
page = urlopen(url).read()
soup = bs(page)

for link in soup.find_all('a'):
    if link.get('href')[-4:] == '.'+filetype:
        down = urljoin(url, link.get('href'))
        split = urlsplit(down)
        filename = split.path.split("/")[-1]
        f = urlopen(down)
        data = f.read()
        if not path.exists("out"):
            makedirs("out")
        with open(+filename, "wb") as code:
            code.write(data)
            print "Downloaded " + filename