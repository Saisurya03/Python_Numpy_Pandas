from bs4 import BeautifulSoup
page = "<html><head><title>A simple example</title></head><body><p>Python for Data Science</p></body></html>"
soup = BeautifulSoup(page, "html.parser")
html = list(soup.children)
print(html)
