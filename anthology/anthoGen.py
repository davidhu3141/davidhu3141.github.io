import sys
sys.path.append('./module')

import json
import bytify
import pageGen
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


# MODULE: article list generate
articleListString = pageGen.articleListGen(fromFolder, saveFolder, webResourceRoot)


# MODULE: HTML content generate
pageGen.articleGen(fromFolder, saveFolder, webResourceRoot, articleListString, templeteString)


# MODULE: Index page generate
indexTempletePath = confJson['indexTempletePath']
pageGen.indexPageGen(indexTempletePath, articleListString)
