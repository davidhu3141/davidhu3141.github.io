import sys
import json

# templete file
templeteFile = open('templete.html', 'r')
templeteString = templeteFile.read()

# json file
jsonArticleListFile = open('generate_conf.json', 'r')
jsonArticleListString = jsonArticleListFile.read()
jsonArticleList = json.loads(jsonArticleListString)
jsonArticleList = byteify(jsonArticleList)

articles = jsonArticleList['articles']
initialPath = jsonArticleList['initialpath']
saveFolder = 'tempHTML/'

for o in articles:
	particularPath = o['path']
	saveFilename = particularPath
	articleBody = loadAllContent(initialPath + particularPath)
	MixedString = templeteString.replace('<!--@Article-->', articleBody).replace('<!--@RootPath-->', 'https://davidhu3141.github.io');

	# save file
	outputfile = open(saveFolder + saveFilename, 'w+');
	outputfile.write(MixedString);
