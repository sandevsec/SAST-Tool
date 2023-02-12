import requests
from bs4 import BeautifulSoup

url = "https://upstox.com/open-demat-account/?f=5GBLTB"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

script_tags = soup.find_all("script")

for script in script_tags:
    print(script.text)
