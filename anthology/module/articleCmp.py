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

	setkeysrc = set(src.keys())
	setkeydst = set(dst.keys())
	commonkey = setkeysrc.intersection(setkeydst)
	detachedCat = setkeydst - setkeysrc
	notgenCat = setkeysrc - setkeydst

	return detachedCat, notgenCat, commonkey
	
