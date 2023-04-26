from bs4 import BeautifulSoup
import requests
import pyautogui
import time


date = "25-Apr-2023"
cityCode = "64"
city = "kanpur"
page = "12"
response = requests.get(
    "https://epaper.jagran.com/epaper/" + date + "-" + cityCode + "-" + city + "-edition-" + city + "-page-" + page + ".html")
soup = BeautifulSoup(response.text, "lxml")

# extract paper link
id = "#image" + page
imageTag = soup.select(id)

# write to text file
f = open("imageLink.txt", "w")
link = str(imageTag[0].get('data-src'))
f.write(link)

time.sleep(1)
location = pyautogui.locateOnScreen('notification.png')
print(location)
