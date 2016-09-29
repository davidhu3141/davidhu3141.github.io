import sys
sys.path.append('./shell')

import json
from os import walk
from os import makedirs
from os import path
import bytify

# json file
confJsonFile = open('templete/conf.json', 'r')
confJsonString = confJsonFile.read()
confJson = json.loads(confJsonString)
confJson = bytify.byteify(confJson)

# templete file
templeteFile = open(confJson['templetePath'], 'r')
templeteString = templeteFile.read()

# other generate settings
webResourceRoot = confJson['webResourceRoot']
fromFolder = confJson['sourcePath']
saveFolder = confJson['destinationPath']

# article list pregenerate
categoryStruct = {}
for (dirpath, dirnames, filenames) in walk(fromFolder):
	for filename in filenames:
		if filename.endswith('.html'):
			
			categoryName = ''.join(dirpath).replace(confJson['sourcePath'] + '/', '')
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
		articleListString += '<div class="articleLink"><a href="' + confJson['webResourceRoot'] + confJson['destinationPath'] + '/' + c + '/' + f + '.html' + '">' + f + '</a></div>\n'
	articleListString += '</div>\n'

	articleListString += '</div>\n'
		
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

# index file
indexTempleteFile = open('indexTemplete.html', 'r')
indexTempleteString = indexTempleteFile.read()

#indexContent = open('indexContent.html', 'r')
indexContentString = ''#indexContent.read()

MixedString = indexTempleteString
MixedString = MixedString.replace('<!--@Article-->', indexContentString);
MixedString = MixedString.replace('<!--@ArticleList-->', articleListString)

outputIndexFile = open('index.html', 'w+')
outputIndexFile.write(MixedString)