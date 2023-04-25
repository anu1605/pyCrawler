from bs4 import BeautifulSoup
import requests
response = requests.get(
    "https://epaper.jagran.com/epaper/25-Apr-2023-64-kanpur-edition-kanpur-page-11.html")
soup = BeautifulSoup(response.text, "lxml")


link = soup.select("#image11")
print(link[0])
