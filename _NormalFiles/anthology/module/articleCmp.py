from os import walk
from os import path

# generate file structure
def fileStruct(folder):

	categoryStruct = {}
	for (dirpath, dirnames, filenames) in walk(folder):
		for filename in filenames:
			if filename.endswith('.html'):
			
				categoryName = ''.join(dirpath).replace(folder + '/', '')
				titleName = filename.replace('.html', '')
			
				if categoryName not in categoryStruct:
					categoryStruct[categoryName] = []
			
				categoryStruct[categoryName].extend([titleName])

	return categoryStruct


# compare file struct
def fileStructCmp(src, dst):

	setcatsrc = set(src.keys())
	setcatdst = set(dst.keys())
	commondir = setcatsrc.intersection(setcatdst)
	notgencat = setcatsrc - setcatdst

	notgenart = set()

	for dir in commondir:
		srcart = set(src[dir])
		dstart = set(dst[dir])
		notgenart.union(srcart - dstart)

	return notgencat, notgenart
	
