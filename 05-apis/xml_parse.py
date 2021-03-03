from urllib.request import urlopen
from xml.etree.ElementTree import parse

"""
Parses an RSS feed using xml ElementTree
"""

feed = urlopen('https://www.yahoo.com/news/rss/world')
xmldoc = parse(feed)
root = xmldoc.getroot()

for entry in root.iter('item'):
    title = entry.find('title')
    print(title.text)
