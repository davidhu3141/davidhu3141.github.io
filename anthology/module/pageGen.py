from os import walk
from os import makedirs
from os import path

### article list pregenerate
def articleListGen(fromFolder, saveFolder, webResourceRoot):

	categoryStruct = {}
	for (dirpath, dirnames, filenames) in walk(fromFolder):
		for filename in filenames:
			if filename.endswith('.html'):
			
				categoryName = ''.join(dirpath).replace(fromFolder + '/', '')
				titleName = filename.replace('.html', '')
			
				if categoryName not in categoryStruct:
					categoryStruct[categoryName] = []
			
				categoryStruct[categoryName].extend([titleName])

	# article list generate
	articleListString = ''
	for c in categoryStruct:

		categoryStruct[c] = sorted(categoryStruct[c], key=str.lower)

		articleListString += '<div class="category">\n'
		articleListString += '<div class="categoryTitle">' + c + '</div>\n'

		articleListString += '<div class="categoryList">\n'
		for f in categoryStruct[c]:
			articleListString += '<div class="articleLink"><a href="' + webResourceRoot + saveFolder + '/' + c + '/' + f + '.html' + '">' + f + '</a></div>\n'
		articleListString += '</div>\n'
	
		articleListString += '</div>\n'

	return articleListString


### HTML content generate
def articleGen(fromFolder, saveFolder, webResourceRoot, articleListString, templeteString):
	
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


### index file generate
def indexPageGen(indexTempletePath, articleListString):
	indexTempleteFile = open(indexTempletePath, 'r')
	indexTempleteString = indexTempleteFile.read()

	#indexContent = open('indexContent.html', 'r')
	indexContentString = ''#indexContent.read()

	MixedString = indexTempleteString
	MixedString = MixedString.replace('<!--@Article-->', indexContentString);
	MixedString = MixedString.replace('<!--@ArticleList-->', articleListString)

	outputIndexFile = open('index.html', 'w+')
	outputIndexFile.write(MixedString)
	outputIndexFile.close()
