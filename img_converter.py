import time
import sys
from scrapper import getUrlContent, getImageUrl, downloadImage
from webp import load_images, convert_to_webp
from colorama import Fore, Style
from urllib.parse import urlparse
from img_class import IMG_FILE

def main():

    if (len(sys.argv) <= 1) :
        return

    verbose = '--verbose' in sys.argv 

    print ('Crawling urls...')
    base_url = sys.argv[1]
    urlSet = set()
    urlSet.add(base_url)
    domain = urlparse(base_url).netloc
    soup = getUrlContent(base_url)

    for link in soup.find_all('a') :
        page = link.get('href')
        if page and page.startswith('http') and (domain in page):
            urlSet.add(page)

    if (verbose) : print(urlSet)

    print ('Scraping images...')
    imageSet = set()
    for url in urlSet :
        getImageUrl(url, imageSet)

    print ('Downloading images...')
    for imgUrl in imageSet :
        downloadImage(imgUrl)

    images = load_images()

if __name__ == "__main__":
    main()