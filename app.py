import subprocess
from bs4 import BeautifulSoup
import requests
import time

response = requests.get(
    "https://epaper.jagran.com/epaper/25-Apr-2023-64-kanpur-edition-kanpur-page-11.html")
soup = BeautifulSoup(response.text, "lxml")


link = soup.select("#image11")
f = open("php/imageLink.txt", "w+")
f.write(str(link[0].get('data-src')))


# time.sleep(5)
# result = subprocess.run(
#     ['php', 'php/index.php'],
#     stdout=subprocess.PIPE,
#     check=True,

# )

# print(result.stdout)
