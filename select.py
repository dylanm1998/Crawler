from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')

# (1) Find by tag name
print(soup.select('a'))
# (2) Find by class name
print(soup.select('.sister'))
# (3) Find by ID
print(soup.select('#link1'))
# (4) Combination search
print(soup.select('p #link1'))
print(soup.select('head > title'))
# (5) Find by attribute
print(soup.select('a[href="http://example.com/elsie"]'))
# (6) Get content
print(soup.select('title')[0].get_text())

