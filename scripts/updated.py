import datetime

dt = datetime.datetime.now()
date = dt.strftime("%c")

file = open("../views/updated.html", "w")
file.write('<p class="updated"><i>Updated: ' + date + '</i></p>')
file.close()
print(date + " update doned")
