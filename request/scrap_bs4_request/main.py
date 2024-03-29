from bs4 import BeautifulSoup
import requests


x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)
print("ُلام")