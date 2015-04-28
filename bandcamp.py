from bs4 import BeautifulSoup 
import requests, re, json, sys, os, getpass

def getVar(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    script=  soup.find_all("script")[7]
    string = script.string
    return string

def getData(string):
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

def getTrackName(url):
    lst = url.split('/')
    track = lst[4]
    return track

def getAlbumName(url):
    lst = url.split('/')
    album = str(lst[2]).split('.')[0]
    return album
def createDir():
    path = " "
    if sys.platform == "linux" or sys.platform == "linux2":
        path = "/home/"+ getpass.getuser()+"/Downloads/Bandcamp-dl"
    elif sys.platform == "win32":
        path = "C:\Users\\" + getpass.getuser() + "\Downloads\Bandcamp-dl"
        
    if not os.path.exists(path):
        cmd = "mkdir "+ path
        os.system(cmd)
   
    return path

def writeFile(stream_url, track ):
    r = requests.get(stream_url, stream = True)
    path =  createDir()
    path =  path + "/" + track+".mp3"
    if r.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)
  
def main():
    url = sys.argv[1]
    string = getVar(url)
    track  = getTrackName(url)
    stream_url = getData(string)
    writeFile(stream_url, track)
  
if __name__== "__main__":
    main()
