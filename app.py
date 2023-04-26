import subprocess
from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://epaper.jagran.com/epaper/25-Apr-2023-64-kanpur-edition-kanpur-page-11.html")
soup = BeautifulSoup(response.text, "lxml")

# print(soup)
link = soup.select("#image11")
f = open("imageLink.html", "w+")
f.write(str(link[0].get('data-src')))


result = subprocess.run(
    ['php', 'php/index.php'],    # program and arguments
    stdout=subprocess.PIPE,  # capture stdout
    check=True,
)

print(result.stdout)
