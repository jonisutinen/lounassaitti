import urllib
import json
import datetime
from collections import OrderedDict


year = datetime.datetime.today().year
month = datetime.datetime.today().month
day = datetime.datetime.today().day

URL = 'https://www.sodexo.fi/ruokalistat/output/weekly_json/28009/' + str(year) + '/' + str(month) + '/' + str(day) + '/fi'
jsonDoku = urllib.urlopen(URL).read();

string = ''
djson = json.loads(jsonDoku.decode('utf-8'), object_pairs_hook = OrderedDict)
menut = djson['menus']
for menus in menut:
    if menus == 'monday':
        string += '<h2>Maanantai</h2><br>'
    if menus == 'tuesday':
        string += '<h2>Tiistai</h2><br>'
    if menus == 'wednesday':
        string += '<h2>Keskiviikko</h2><br>'
    if menus == 'thursday':
        string += '<h2>Torstai</h2><br>'
    if menus == 'friday':
        string += '<h2>Perjantai</h2><br>'
    if menus == 'saturday':
        string += '<h2>Lauantai</h2><br>'
    if menus == 'sunday':
        string += '<h2>Sunnuntai</h2><br>'
    paiva = menut[menus]
    for i in paiva:
        string += '<table><tr>'
        try:
            string += i['title_fi'] + ' (' + i['properties'] + ')</tr><br>'
        except KeyError:
            string += i['title_fi'] + '</tr><br>'
        string += '<tr>'
        string += i['price'] + '</tr></table>'


file = open("../views/opistotie.html", "w")
file.write(string.encode('utf-8'))
file.close()
print("opistotie doned")
