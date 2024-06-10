import time
import sys
from scrapper import getUrlContent, getImageUrl, downloadImage
from webp_converter import load_images, convert_to_webp

def main():

    if (len(sys.argv) <= 1) :
        return

    print ('Crawling urls...')
    base_url = sys.argv[1]
    urlSet = set()
    urlSet.add(base_url)

    soup = getUrlContent(base_url)
    for link in soup.find_all('a') :
        page = link.get('href')
        if "service-public" in page :
            urlSet.add(page)

    print ('Scraping images...')
    imageSet = set()
    for url in urlSet :
        getImageUrl(url, imageSet)

    print ('Downloading images...')
    for imgUrl in imageSet :
        downloadImage(imgUrl)

    print ('Converting png and jpg to webp...')

    images = load_images()
    for img in images :
        convert_to_webp(img)

    # for image in imageSet :
    #     print(image)
    # for urls in urlSet : 
    #     print(urls)

if __name__ == "__main__":
    main()