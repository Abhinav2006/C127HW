from bs4 import BeautifulSoup
import requests

starturl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/abhin/Downloads/chromedriver_win32 (1)/chromedriver")
browser.get(starturl)

Data = []
newData = []

headers = ["Name", "Distance", "Mass", "Radius"]