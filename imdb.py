import requests
from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"

#response = requests.get(url)
#content = response.content
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find('tbody',{"class":"lister-list"}).find_all("tr",limit=10)
count = 0

for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    count += 1

    print(f"{count}- Film: {title} yıl: {year} değerlendirme: {rating}")
