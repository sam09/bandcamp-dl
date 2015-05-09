from bs4 import BeautifulSoup 
import requests, re, json, sys, os, getpass

def getVar(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    script=  soup.find_all("script")[7]
    string = script.string
    return string

def getUrl(string):
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

def getAlbumName(string):
    search = "album_title : \""
    startIndex = string.find(search) + len(search)
    endIndex = string.find("\"", startIndex)
    albumName = string[startIndex:endIndex]
    return albumName

def getTrackName(url):
    lst = url.split('/')
    track = lst[4]
    return track

def getArtistName(url):
    lst = url.split('/')
    artist = str(lst[2]).split('.')[0]
    return artist

def removeSpecialChars(album):
    special = [' ' , ':', ',', ',' '(', ')', '-']
    newName = ""
    for i in album:
        if i in special:
           newName += "_"
        else:
           newName += i
    return newName

def createDir(album, artist):
    path = " "
    if sys.platform == "linux" or sys.platform == "linux2":
        path = "/home/"+ getpass.getuser()+"/Downloads/Bandcamp-dl"
    elif sys.platform == "win32":
        path = "C:\Users\\" + getpass.getuser() + "\Downloads\Bandcamp-dl"
        
    if not os.path.exists(path):
        cmd = "mkdir "+ path
        os.system(cmd)
    if sys.platform == "linux" or sys.platform == "linux2":
        path = path + "/" + artist
    elif sys.platform == "win32":
        path = path + "\\" + artist

    if not os.path.exists(path):
        cmd = "mkdir " + path
        os.system(cmd)

    album = removeSpecialChars(album)

    if sys.platform == "linux" or sys.platform == "linux2":
        path = path + "/" + album
    elif sys.platform == "win32":
        path = path + "\\" + album

    if not os.path.exists(path):
        cmd = "mkdir " + path
        os.system(cmd)

    return path

def writeFile(stream_url, track, album, artist):
    r = requests.get(stream_url, stream = True)
    path =  createDir(album, artist)
    path =  path + "/" + track+".mp3"
    if r.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)
  
def main():
    url = sys.argv[1]
    string = getVar(url)
    track  = getTrackName(url)
    stream_url = getUrl(string)
    artist = getArtistName(url)
    album = getAlbumName(string)
    writeFile(stream_url, track, album, artist)
 
if __name__== "__main__":
    main()
