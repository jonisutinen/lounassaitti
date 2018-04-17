import urllib
from bs4 import BeautifulSoup
import datetime


paiva = datetime.datetime.today().weekday()
dt = datetime.datetime.now()
wk = dt.isocalendar()[1]

year = datetime.datetime.today().year

URL = 'https://www.servica.fi/ruokalistat/?lista=savotalo&vko=' + str(wk) + '&vuosi=' + str(year) + '#savotalo'
html = urllib.urlopen(URL).read()

soup = BeautifulSoup(html, 'html.parser')

savotalo = soup.find('div', attrs={'id':'savotalo'})
savotalo2 = savotalo.find('div', attrs={'class': 'menu-weekday-wrap'})
file = open("../views/tk.html", "w")
head = open("../head/head.html", "r")
headread = head.read()
file.write(headread + "\n" + str(savotalo2) + "\n" + "</body></html>")
file.close()
head.close()
print("tk doned")
