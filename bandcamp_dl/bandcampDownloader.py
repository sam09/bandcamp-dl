from bs4 import BeautifulSoup 
import requests, re, json, os

class Downloader():

	def __init__( self, url = None):
		self.url = url
		
	def get_HTML(self):
		url  = self.url 
		r = requests.get(url)
		soup = BeautifulSoup(r.text)
		script=  soup.find_all("script")[7]
		string = script.string
		return string

	def get_album_name(self):
		string = self.string
		search = "album_title : \""
		startIndex = string.find(search) + len(search)
		endIndex = string.find("\"", startIndex)
		albumName = string[startIndex:endIndex]
		albumName = self.remove_special_chars(albumName)
		return albumName

	def get_track_name(self):
		url = self.url
		lst = url.split('/')
		track = lst[4]
		return track

	def get_artist_name(self):
		url  = self.url
		lst = url.split('/')
		artist = str(lst[2]).split('.')[0]
		return artist

	def remove_special_chars(self, album):
		special = [' ' , ':', ',', ',' '(', ')', '-']
		newName = ""
		for i in album:
			if i in special:
				newName += "_"
			else:
				newName += i
		return newName

	def get_stream_url(self):
		string = self.string
		search = "var TralbumData = "
		startIndex =  string.find(search) + len(search)
		endIndex = string.find(";", startIndex)
		trackinfo =  string[startIndex:endIndex]
    
		search = "trackinfo:"
		startIndex = trackinfo.find("trackinfo:")+len(search)
		endIndex = trackinfo.find("],", startIndex) + len("]")

		parsed = json.loads(trackinfo[startIndex:endIndex])[0]
		stream_url =  parsed["file"]["mp3-128"]
		return stream_url

	def write_file(self):
		path = "Songs"
		if not os.path.exists(path):
			os.makedirs(path)
		
		path =  path + "/" + self.artist + "_" + self.track+".mp3"
	
		r = requests.get(self.stream_url, stream = True)	
		if r.status_code == 200:
			with open(path, 'wb') as f:
				for chunk in r.iter_content():
					f.write(chunk)

	def download(self):
		print "Connecting..."
		url = self.url
		self.string = self.get_HTML()
		self.track  = self.get_track_name()
		self.stream_url = self.get_stream_url()
		print "File Found"
		self.artist = self.get_artist_name()
		self.album = self.get_album_name()
		print "Downloading File"
		self.write_file()
 
