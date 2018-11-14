import sys
import urllib2

response = urllib2.urlopen('http://news.google.com/')
html = response.read()
sys.stdout.write(html)
