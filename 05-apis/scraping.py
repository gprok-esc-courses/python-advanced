import requests
from bs4 import BeautifulSoup

"""
Extracts job titles from a job vacancies web page
using Beautiful Soup for web scraping
"""

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=New-York'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('h2', class_='title')

for item in results:
    print(item.text)
