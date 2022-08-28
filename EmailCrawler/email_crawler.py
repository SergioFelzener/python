## ferramenta de enumeração de paginas / diretorios / arquivos (mapear o website)
from ast import While
import requests
import sys
from bs4 import BeautifulSoup
import re
import collections
collections.Callable = collections.abc.Callable

## criando listas principais 
TO_CRAWL = []
## Guarda todas urls do crawling
CRAWLED = set()
EMAILS = []

def request(url):
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"}
    try:
        response = requests.get(url, headers=header)
        return response.text
    except KeyboardInterrupt:
        sys.exit()
    except Exception as error:
        print("Request Error : " , error)
        pass
    

def get_links(html):
    links = []
    try:
        soup = BeautifulSoup(html, "html.parser")
        tags_a = soup.find_all("a", href=True)
        for tag in tags_a:
            link = tag["href"]
            if link.startswith("http"):
                links.append(link)
            
        return links    
    except Exception as error:
        print("Error : ",error)
        pass
    
def get_emails(html):
    emails = re.findall(r"\w[\w\ . ]+\w@\w[\w\ .]+\w", html)
    return emails


def crawl():
    while 1:
        if TO_CRAWL:
            url = TO_CRAWL.pop()
            # response = requests.get(url) resposta commentada pois foi criada uma função que fará o request 
            html = request(url)
            if html:
                links = get_links(html)
                if links:
                    for link in links:
                        if link not in CRAWLED and link not in TO_CRAWL:
                            TO_CRAWL.append(link)
                            
                emails = get_emails(html)
                for email in emails:
                    if email not in EMAILS:
                     
                        print(email)
                        EMAILS.append(email)
               
                CRAWLED.add(url)
            else:
                CRAWLED.add(url)          
        else:
            print("Done")
            break
        
if __name__ == "__main__":
    url = sys.argv[1]
    TO_CRAWL.append(url)
    crawl()
    