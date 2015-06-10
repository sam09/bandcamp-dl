# Bandcamp-dl

A simple module which can download the audio at a particular url on bandcamp.com


| Version | Downloads |
| --------| --------- |
 [![Latest Version](https://pypip.in/v/ImageScraper/badge.png)](https://pypi.python.org/pypi/bandcamp_dl/) |[![PyPi downloads](http://img.shields.io/badge/downloads-18k%20total-blue.svg)](https://pypi.python.org/pypi/bandcamp_dl)

==================================================================
###Installation

####From Source
* Clone the repo or download the zip
* Make sure you have pip installed
* `cd` to the folder
* `pip -install -r "requirements.txt"`
* `python bandcamp.py <url>`

####Using pip
* pip install bandcamp_dl

==================================================================
###Usage
`from bandcamp_dl import bandcampDownloader`

`dl = bandcampDownloader.Downloader(url)`

`dl.download()`

==================================================================
###Dependencies
* BeautifulSoup - HTML parsing
* Requests - for retrieving HTML

==================================================================
###Note
All tracks are stored at Songs folder at the current directory

==================================================================
####Contribute
If you want to add features, improve them, or report issues, feel free to send a pull request!!

####Author
[sam09] (https://github.com/sam09) ([Sam Radhakrishnan](https://twitter.com/sam_rk9))
