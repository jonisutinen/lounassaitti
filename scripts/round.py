import urllib
from bs4 import BeautifulSoup

URL = 'https://www.antell.fi/lounaslistat/lounaslista.html?owner=79'
html = urllib.urlopen(URL).read()

soup = BeautifulSoup(html, 'html.parser')

paivays = soup.find('td', attrs={'class': 'main-title'})
span = paivays.find_all('span')

taulukko = soup.find('table', attrs={'id': 'lunch-content-table'})
ruoka = taulukko.find_all('table', attrs={'class':'show'})

string = ''
for n in span:
    string += str(n) + '<br>'
string += '<br>'

for i in ruoka:
    string += str(i)

file = open("../views/round.html", "w")
file.write(string)
file.close()
print("round doned")
