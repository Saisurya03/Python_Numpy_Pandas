from bs4 import BeautifulSoup
import requests

url = "file:///C:/Users/123/Downloads/test.html"

html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
print(soup.prettify())
