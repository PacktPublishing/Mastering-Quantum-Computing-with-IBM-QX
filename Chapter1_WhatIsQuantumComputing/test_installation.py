import sys
# The following code tests your Python installation

try:
	import numpy
	import matplotlib
except:
	raise Exception("make sure to pip install -r requirements.txt")



if not (sys.version_info > (3, 0)):
	raise Exception("You are running Python 2. Python 3.4+ is required for code examples")

