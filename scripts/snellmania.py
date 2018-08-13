import urllib
import json
import datetime

dt = datetime.datetime.now()

dturl = dt.strftime("%Y-%m-%d")

url = "https://www.fazerfoodco.fi/api/restaurant/menu/week?language=fi&restaurantPageId=180123&weekDate=" + dturl
jsonDoku = urllib.urlopen(url).read();

djson = json.loads(jsonDoku)

menut = djson['LunchMenus']

string = ''
for day in menut:
    string += '<h2>' + day['DayOfWeek'] + ' ' + day['Date'] + '</h2>' + '<br>'
    nimi = day['SetMenus']
    string += "<table class='days'>"
    for name in nimi:
        string += "<tr>"
        string += '<td><b>' + name['Name'] + '</b> '
        if name['Price'] is None:
            string += ''
        else:
            string += '<i>' + name['Price'] + '</i>'
        string += '</td>'
        string += '</tr>'
        string += '<tr>'
        meals = name['Meals']
        string += '<td>'
        for i in meals:
            string += i['Name'] + ' '
            diets = i['Diets']
            string += '<i>'
            for n in diets:
                string += n + ', '
            string += '</i><br>'
        string += '<br>'
        string += '</td>'
    string += '</table>'

file = open("../views/snellmania.html", "w")
head = open("../head/snellmaniahead.html", "r")
headread = head.read()
file.write(headread + "\n" + string.encode('utf-8') + "\n" + "</body></html>")
file.close()
head.close()

print("snellmania doned")
