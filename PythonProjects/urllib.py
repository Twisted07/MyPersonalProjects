#!/usr/bin/python3

import urllib3.request, urllib3.parse, urllib3.error

hello = urllib3.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in hello:
	print(line.decode().strip())
