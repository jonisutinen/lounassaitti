import urllib
from bs4 import BeautifulSoup

URL = 'https://www.antell.fi/lounaslistat/lounaslista.html?owner=79'
html = urllib.urlopen(URL).read()

soup = BeautifulSoup(html, 'html.parser')

taulukko = soup.find('div', attrs={'class': 'lunch-menu-language state--active'})

file = open("../views/round.html", "w")
file.write(str(taulukko))
file.close()
print("round doned")
