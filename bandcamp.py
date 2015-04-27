from bs4 import BeautifulSoup 
import requests, re, json, sys

def getVar(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    script=  soup.find_all("script")[7]
    string = script.string
    return string
def getData(string):
    x = string.find("var TralbumData =")+17
    y = string.find(";", x)
    p = string[x:y]
    a = p.find("trackinfo:")+10
    b = p.find("],",a)+1
    parsed = json.loads(p[a:b])[0]
    stream_url =  parsed["file"]["mp3-128"]
    return stream_url

def getTrackName(url):
    lst = url.split('/')
    track = lst[4]
    album = str(lst[2]).split('.')[0]
    print album
    return track

def writeFile(stream_url, track ):
    r = requests.get(stream_url, stream = True)
    path = "songs/"+track+".mp3"
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
