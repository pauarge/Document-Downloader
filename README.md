#Document Downloader

As a university student, I get most of the studying stuff through the Internet. Most professors give me a URL where I can download all the required files to work (mostly, PDF theory files). The problem is that usually in that pages there are lots of files, and manually download all of them

I did this simple script to massively download files from a webpage which has all the links in it.  



##Requirements

This script runs on Python 2.7 (I'm working on a Python 3 version), so if you have Python installed in your computer, it should work! I've tested heavily on a Mac and Linux (Ubuntu), but if you have a Windows machine, you shouldn't have any problem. If you don't have Python installed, please refer [here](https://www.python.org/downloads/).

You need [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/) to run it. The other packages we are using are bundled by default with any Python instalation. 

If you don't use a package manager for Python, I highly recommend [PIP](https://pip.pypa.io/en/latest/quickstart.html) (and [VirtualEnv](https://virtualenv.pypa.io/en/latest/)). Then, installing BS4 it's really easy:

`pip install beautifulsoup4`

##How it works