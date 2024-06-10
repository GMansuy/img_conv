from bs4 import BeautifulSoup
import urllib.request
import requests
import os

def getUrlContent(url) :
    content = requests.get(url).content
    return BeautifulSoup(content, 'html.parser')

def getImageUrl(url, imageSet):
    htmldata = requests.get(url).text
    soup = BeautifulSoup(htmldata, 'html.parser')
    for item in soup.find_all('img') :
        imageSet.add(item['src'])

def downloadImage(imgUrl):
    if imgUrl.endswith('/') :
        print('Error')
        return

    nameIndex = imgUrl.rfind('/')
    if -1 != nameIndex :
        imgName = imgUrl[nameIndex + 1:]
    else :
        imgName = imgUrl
    
    if imgUrl.startswith('https') :
        output = os.path.curdir + '/images/' + imgName
        urllib.request.urlretrieve(imgUrl, output)
