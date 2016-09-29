from os import walk
from os import makedirs
from os import path

def articleGen(fromFolder, saveFolder, webResourceRoot, articleListString, templeteString):

	# HTML content generate
	for (dirpath, dirnames, filenames) in walk(fromFolder):
		for filename in filenames:
			if filename.endswith('.html'):

				loadPath = ''.join(dirpath) + '/' + filename
				savePath = loadPath.replace(fromFolder, saveFolder)

				articleBodyString = open(loadPath, 'r').read()
				MixedString = templeteString
				MixedString = MixedString.replace('<!--@WebResourceRoot-->', webResourceRoot)
				MixedString = MixedString.replace('<!--@Article-->', articleBodyString)
				MixedString = MixedString.replace('<!--@ArticleList-->', articleListString)

				if not path.exists(path.dirname(savePath)):
					makedirs(path.dirname(savePath))

				outputfile = open(savePath, 'w+')
				outputfile.write(MixedString)
				outputfile.close();
