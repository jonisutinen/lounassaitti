import urllib
from bs4 import BeautifulSoup

URL = 'https://www.antell.fi/lounaslistat/lounaslista.html?owner=79'
html = urllib.urlopen(URL).read()

soup = BeautifulSoup(html, 'html.parser')
taulukko = soup.find('table', attrs={'id': 'lunch-content-table'})
ruoka = taulukko.find_all('table', attrs={'class':'show'})

string = ''

for i in ruoka:
    string += str(i)

file = open("../views/round.html", "w")
file.write(string)
file.close()
print("round doned")
