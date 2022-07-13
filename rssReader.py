from bs4 import BeautifulSoup
import requests
import lxml
url= requests.get('https://rss.nytimes.com/services/xml/rss/nyt/MiddleEast.xml')

soup= BeautifulSoup(url.content,'xml')
entries= soup.find_all('item')

for en in entries:
    title= en.title.text
   # smry=en.summary.text
    #link=en.link['href']
    print(f"Title={title}")
    #print(f"Summary={smry}")
    #print(f"Link={link}")