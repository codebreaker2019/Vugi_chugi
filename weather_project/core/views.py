from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.

toi_r = requests.get("https://www.thedailystar.net/frontpage/news/covid-vaccine-still-possible-year-1959229/")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')
toi_headings = toi_soup.find_all('h2')
toi_news = []

for t in toi_headings:
    toi_news.append(t.text)

ht_r = requests.get("https://www.who.int/emergencies/diseases/novel-coronavirus-2019?gclid=Cj0KCQjwhvf6BRCkARIsAGl1GGjXm2YI07MVfr4SxBhxSxrUnN-K-FaArBKWgEqb9xENulPETDZ29_oaAus2EALw_wcB/")
ht_soup = BeautifulSoup(ht_r.content, 'html.parser')
#ht_headings = ht_soup.findAll("div", {"class":"sf-item-header-wrapper"})
ht_paragraph = ht_soup.find_all('p')
#ht_headings = ht_headings[2:]
ht_news = []

#for hth in ht_paragraph:
#    ht_news.append(hth.text)
for ht in ht_paragraph:
    ht_news.append(ht.text)


def home(request):
    return render(request,'core/home.html',{'toi_news':toi_news,'ht_news':ht_news})
