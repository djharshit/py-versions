import requests
from bs4 import BeautifulSoup

try:
    res = requests.get("https://www.python.org/downloads/")
    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.find_all(name="ol", class_="list-row-container menu")[1]
    version = items.find_all(name="span", class_="release-number")
    date = items.find_all(name="span", class_="release-date")

    for i in range(10):
        print(version[i].text, date[i].text)

except:
    print("Not connected")

finally:
    input()
