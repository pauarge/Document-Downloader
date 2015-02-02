from bs4 import BeautifulSoup as bs
from os import path, makedirs, system
from urllib2 import urlopen
from urlparse import urljoin, urlsplit
import time
import sys
import argparse


def parse_outpath(outpath):
    if outpath[-1:] != '/':
        return outpath + '/'
    else:
        return outpath


def parse_url(url):
    if url[:7] != 'http://' and url[:8] != 'https://':
        return 'http://' + url
    else:
        return url


def parse_filetype(filetype):
    if filetype[:1] != '.':
        return '.'+filetype, len(filetype) + 1
    else:
        return filetype, len(filetype)


def main(argv):

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--outpath')
    parser.add_argument('-u', '--url')
    parser.add_argument('-f', '--filetype')
    args = parser.parse_args()

    if args.outpath:
        outpath = parse_outpath(args.outpath)
    else:
        outpath = 'out/'

    if args.url:
        url = parse_url(args.url)
    else:
        print ("Please, write the URL where you want to download from")
        url = parse_url(raw_input())

    if args.filetype:
        filetype, filetype_len = parse_filetype(args.filetype)
    else:
        print ("What kind of file you wanna download?")
        filetype, filetype_len = parse_filetype(raw_input())

    count = 0
    start_time = time.time()
    page = urlopen(url).read()
    soup = bs(page)

    for link in soup.find_all('a'):
        if link.get('href')[-filetype_len:] == filetype:
            down = urljoin(url, link.get('href'))
            split = urlsplit(down)
            filename = split.path.split("/")[-1]
            f = urlopen(down)
            data = f.read()
            if not path.exists(outpath):
                makedirs(outpath)
            with open(outpath+filename, "wb") as code:
                code.write(data)
                partial_time = str(round(time.time()-start_time, 2))
                count += 1
                print ("Downloaded " + filename + ' (' + partial_time + ' seconds elapsed)')

    final_time = str(round(time.time()-start_time, 2))

    print ("\n Downlaoded " + str(count) + " files in " + final_time + " seconds.")


if __name__ == '__main__':
    system('clear')
    main(sys.argv[1:])