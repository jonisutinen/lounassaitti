import urllib
from bs4 import BeautifulSoup
import datetime

year = datetime.datetime.today().year
month = datetime.datetime.today().month
day = datetime.datetime.today().day

URL = 'https://www.sodexo.fi/ruokalistat/output/weekly_html/28009/' + str(year) + '/' + str(month) + '/' + str(day) + '/fi'
html = urllib.urlopen(URL).read()

soup = BeautifulSoup(html, 'html.parser')

file = open("../views/opistotie.html", "w")
file.write(str(soup))
file.close()
print("opistotie doned")
