import re
import lxml
import html5lib

from bs4 import BeautifulSoup
from urllib import urlopen

class Page(object):
    """
    Attributes:
        title: A string representing the content of <TITLE> tag.
    """

    def __init__(self, name):
        """
	Return a Page object whose name is *title*
	"""
        self.title = title

def getHtml(path):
        return open(path)

def main():
	mySoup = BeautifulSoup(open("xda.html"), "lxml")

	title = mySoup.title.text
	print("Page Title : "+title)

	meta = mySoup("meta")
	#print(meta)

	for m in meta:
		name = m.get("name")
		if name == "keywords" or name == "description" or name == "robots":
			print(name+" content : "+m["content"])

	"""
	for link in mySoup.find_all('a'):
		print(link.get('href'))

	#print(mySoup.get_text())
	#"""


if __name__ == "__main__":
    main()
