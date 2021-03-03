import feedparser

"""
Parses an RSS feed using feedpasrer
"""

feed = feedparser.parse("https://www.yahoo.com/news/rss/world")

print('Number of RSS posts :', len(feed.entries))

for entry in feed.entries:
    print(entry.title)

