#Document Downloader

As a university student, I get most of the studying stuff through the Internet. Most professors give me a URL where I can download all the required files to work (mostly, PDF theory files). The problem is that usually in that pages there are lots of files, and manually download all of them is a pain on the ass.

I did this simple script to massively download files from a webpage which has all the links in it.  



##Requirements

This script runs on Python 2.7 (I'm working on a Python 3 version), so if you have Python installed on your computer, it should work! I've tested heavily on a Mac and Linux (Ubuntu), but if you have a Windows machine, you shouldn't have any problem. If you don't have Python installed, please refer [here](https://www.python.org/downloads/).

You need [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/) to run it. The other packages we are using are bundled by default with any Python instalation. 

If you don't use a package manager for Python (though it's not required), I highly recommend [PIP](https://pip.pypa.io/en/latest/quickstart.html) (and [VirtualEnv](https://virtualenv.pypa.io/en/latest/)). Then, installing BS4 it's really easy:

`pip install beautifulsoup4`

##How it works

* Make sure you have installed and enabled (if you are using a Virtualenv) the packages listed on the requirements. ([How to create and activate a Virtualenv?](http://docs.python-guide.org/en/latest/dev/virtualenvs/))
* Open your terminal (or cmd on Windows) and navigate to the directory where you cloned the repository (typically using `cd`).
* Run the script using `python document-downloader.py`. The following arguments apply:
	* **Outpath** *(-o, --outpath)*: Where you wanna output the files. If not specified, it will output by default on `out/`.
	* **URL** *(-u, --url)*: URL where you want to download the files from. If not specified, it will be propmted during the script execution.
	* **Filetype** *(-f, --filetype)*: The type of file you want to download. If not specified, it will be propmted during the script execution.
	
**NOTE: Optional data on those parameters such as 'http://' for URLS, final slash for outpath or dot for filetype will be added automatically if not specified.**

###Examples:	

`python document-downloader.py -o test -u http://www.cs.upc.edu/~pro1/index.php?id=material-docent -f pdf`

`python document-downloader-py -u www.cs.upc.edu/~pro1/index.php?id=material-docent -f .txt`
 