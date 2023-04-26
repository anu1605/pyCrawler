import subprocess
from bs4 import BeautifulSoup
import requests
import time

date = "25-Apr-2023"
cityCode = "64"
city = "kanpur"
page = "5"
response = requests.get(
    "https://epaper.jagran.com/epaper/" + date + "-" + cityCode + "-" + city + "-edition-" + city + "-page-" + page + ".html")
soup = BeautifulSoup(response.text, "lxml")

id = "#image" + page
link = soup.select(id)
f = open("imageLink.txt", "w+")
f.write(str(link[0].get('data-src')))
