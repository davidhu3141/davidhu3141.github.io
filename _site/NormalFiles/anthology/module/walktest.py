from os import *

for (dirpath, dirnames, filenames) in walk("./"):
	for filename in filenames:
		if filename.endswith('.html'): 
			fullpath = (''.join(dirpath) + '/' + filename).replace('./', '')
			print '<a href="' + fullpath + '">' + filename + "</a>"
