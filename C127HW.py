from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

starturl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(starturl)
soup = bs(page.text, 'html.parser')
starttable = soup.find('table')
tablerows = starttable.find_all('tr')

data = []

for tr in tablerows:
    td = tr.find_all('td')
    row = [i.text.rstrip()for i in td]
    data.append(row)

newData = []

headers = ["Name", "Distance", "Mass", "Radius"]
name = []
distance = []
mass = []
radius = []

for i in range(1, len(data)):
    name.append(data[i][1])
    distance.append(data[i][3])
    mass.append(data[i][5])
    radius.append(data[i][6])

df = pd.DataFrame(list(zip(name, distance, mass, radius)),columns = ['Name', 'Distance', 'Mass', 'Radius'])
df.to_csv('C127HWData.csv')