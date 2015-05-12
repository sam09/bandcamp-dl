from bandcamp_dl import bandcampDownloader
import sys 
  
def main():
	url = sys.argv[1]
	dl  = bandcampDownloader.Downloader(url)
	dl.download()

if __name__== "__main__":
    main()
