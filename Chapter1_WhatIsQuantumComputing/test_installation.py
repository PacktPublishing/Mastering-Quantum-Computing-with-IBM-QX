#!/usr/bin/env python

# The following code tests your Python installation

try:
	import numpy
	import matplotlib
except:
	raise "make sure to pip install -r requirements.txt"

try:
	print ""
	raise "You are running Python 2. Python 3.4+ is required for code examples"
except:
	pass
