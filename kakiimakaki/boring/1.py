from bs4 import BeautifulSoup
import requests

url ="https://www.rbc.ru/"
response = requests.get(url)
web_page = response.text
soup = BeautifulSoup(web_page,"html.parser")
ff = soup.find_all(name = "span", class_="main__big__title")
print(ff[0].get_text())
ss = soup.find_all(name = "span", class_="main__feed__title")
print(ss[0].get_text())
dd = soup.find_all(name = "span", class_="main__feed__title")
print(dd[1].get_text())
