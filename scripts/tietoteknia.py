import xml.etree.ElementTree as ET
import urllib2

URL = 'https://www.fazerfoodco.fi/modules/MenuRss/MenuRss/CurrentWeek?costNumber=0439&language=fi'

xml = urllib2.urlopen(URL)

tree = ET.parse(xml)
root = tree.getroot()

string = ''
for child in root:
    for child2 in child:
        if child2.tag == 'title':
            string += '<h1>' + str(child2.text.encode("utf-8")) + '</h1>'
        if child2.tag == 'item':
            for child3 in child2:
                if child3.tag == 'title':
                    string += '<br><h2>' + str(child3.text.encode("utf-8")) + '</h2><br>'
                if child3.tag == 'description':
                    try:
                        string += str(child3.text.encode("utf-8"))
                    except AttributeError:
                        string += ''

file = open("../views/tietoteknia.html", "w")
head = open("../head/head.html", "r")
headread = head.read()
file.write(headread + "\n" + string + "\n" + "</body></html>")
file.close()
head.close()

print("tietoteknia doned")
