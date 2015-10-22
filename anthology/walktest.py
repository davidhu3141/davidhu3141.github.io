from os import *

for (dirpath, dirnames, filenames) in walk("./"):
	for filename in filenames:
		if filename.endswith('.html'): 
			print ''.join(dirpath) + filename
