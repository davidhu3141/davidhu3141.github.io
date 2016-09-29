import sys
sys.path.append('./module')

import json
import bytify
import articleListGen
import articleGen
from os import walk
from os import makedirs
from os import path

# json file
confJsonFile = open('json/conf.json', 'r')
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

# article list generate
articleListString = articleListGen.articleListGen(fromFolder, saveFolder, webResourceRoot)

# HTML content generate
articleGen.articleGen(fromFolder, saveFolder, webResourceRoot, articleListString, templeteString)

# index file
indexTempleteFile = open(confJson['indexTempletePath'], 'r')
indexTempleteString = indexTempleteFile.read()

#indexContent = open('indexContent.html', 'r')
indexContentString = ''#indexContent.read()

MixedString = indexTempleteString
MixedString = MixedString.replace('<!--@Article-->', indexContentString);
MixedString = MixedString.replace('<!--@ArticleList-->', articleListString)

outputIndexFile = open('index.html', 'w+')
outputIndexFile.write(MixedString)
outputIndexFile.close()
