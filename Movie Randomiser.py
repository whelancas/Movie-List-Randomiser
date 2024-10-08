from urllib.request import Request, urlopen
import urllib.error
from bs4 import BeautifulSoup as bs
import random

def main():
    while True:
        content= []
        while True:
            link = input("Link: ")
            if link[-7:] != "detail/":
                link += "detail/"

            try:
                req = Request(url=link, headers={'User-Agent': 'Mozilla/5.0'})
                content.append(urlopen(req).read().decode('utf8', errors='ignore'))
                break
            except urllib.error.URLError as e:
                print(str(e))

        soup = bs(content[0], features="lxml")
        isMultiplePages = soup.find('div', attrs={'class':'paginate-pages'})

        if isMultiplePages is not None:
            pageNumbers = soup.findAll('li', attrs={'class':'paginate-page'})
            pageCount = pageNumbers[-1].find('a').text

            for i in range(2, int(pageCount)+1):
                newLink = (link + "/page/" + str(i) + "/")
                try:
                    req = Request(url=newLink, headers={'User-Agent': 'Mozilla/5.0'})
                    content.append(urlopen(req).read().decode('utf8', errors='ignore'))
                except urllib.error.URLError as e:
                    print(str(e))

        movies = []
        for item in content:
            soup = bs(item, features="lxml")
            results = soup.find_all('h2', attrs={'class':'headline-2 prettify'})
            
            for movie in results:
                movies.append(movie.find('a').text)

        print(movies[random.randint(0, len(movies)-1)])

if __name__ == "__main__":
    main()