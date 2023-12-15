from urllib.request import Request, urlopen
import urllib.error
from bs4 import BeautifulSoup as bs
import random

def main():
    while True:
        while True:
            link = input("Link: ")
            if link[-7:] != "detail/":
                link += "detail/"

            try:
                req = Request(url=link, headers={'User-Agent': 'Mozilla/5.0'})
                content = urlopen(req).read().decode('utf8', errors='ignore')
                break
            except urllib.error.URLError as e:
                print(str(e))

        soup = bs(content, features="lxml")
        results = soup.find_all('h2', attrs={'class':'headline-2 prettify'})
        
        movies = []
        for movie in results:
            movies.append(movie.find('a').text)

        print(movies[random.randint(0, len(movies)-1)])
    

if __name__ == "__main__":
    main()