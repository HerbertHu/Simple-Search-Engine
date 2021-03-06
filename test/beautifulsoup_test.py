# -*- coding: utf-8 -*-
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(html_doc, 'html.parser')

links = soup.find_all('a')
for link in links:
	print(link.name, link['href'], link.get_text())


link_node = soup.find('a', href='http://example.com/lacie')
print(link_node.name, link_node['href'], link_node.get_text())

link_node_r = soup.find('a', href=re.compile(r"ill"))
print(link_node_r.name, link_node_r['href'], link_node_r.get_text())

link_node_p = soup.find('p', class_ = "title")
print(link_node_p.name, link_node_p.get_text())
