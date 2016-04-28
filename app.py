#!pys/bin/python
import mechanize
from bs4 import BeautifulSoup

# Var store for browser func
browser = mechanize.Browser()

# Parse brand url query
def queryManufacturer(id):
	return '?manufacturer=' + str(id)

# Dictionary of pys brands (unfinished)
def brands(b):
	return {
		'Adidas' : queryManufacturer(370),
		'Puma' : queryManufacturer(467),
		'The Hundreds' : queryManufacturer(498)
	}.get(b, '')

# ::scrape_products::
# Scrapes first page of products, if no brand entered, 
# defaults to home products page
#
# Todo: add pages arg to query multiple pages of products
#########################################################
def scrape_products(url, brand):
	if len(brand) == 0:
		browser.open(url)
	else:
		browser.open(url + brands(brand))
	soup = BeautifulSoup(browser.response().read(), 'html.parser')
	for section in soup.findAll('h2', {'class' : 'product-name'}):
		children = section.findChildren()
		for child in children:
			print child.text

# Tests
scrape_products('http://www.pys.com/shoes', 'Adidas')
scrape_products('http://www.pys.com/shoes', 'Puma')
scrape_products('http://www.pys.com/shoes', 'The Hundreds')