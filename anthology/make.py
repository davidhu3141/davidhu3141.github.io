import sys
import json
from os import walk
from os import makedirs
from os import path
import bytify

# templete file
templeteFile = open('templete.html', 'r')
templeteString = templeteFile.read()

# json file
confJsonFile = open('conf.json', 'r')
confJsonString = confJsonFile.read()
confJson = json.loads(confJsonString)
confJson = bytify.byteify(confJson)

fromFolder = 'stackeditHTML/'
saveFolder = 'generatedHTML/'

for (dirpath, dirnames, filenames) in walk(fromFolder):
	for filename in filenames:
		if filename.endswith('.html'): 

			loadPath = ''.join(dirpath) + '/' + filename
			savePath = loadPath.replace(fromFolder, saveFolder)

			articleBody = open(loadPath, 'r').read()
			MixedString = templeteString.replace('<!--@Article-->', articleBody)

			if not path.exists(path.dirname(savePath)):
				makedirs(path.dirname(savePath))

			outputfile = open(savePath, 'w+');
			outputfile.write(MixedString);

#for o in articles:
#	particularPath = o['path']
#	saveFilename = particularPath
#	articleBody = loadAllContent(initialPath + particularPath)
#	MixedString = templeteString.replace('<!--@Article-->', articleBody).replace('<!--@RootPath-->', 'https://davidhu3141.github.io');
#
#	# save file
#	outputfile = open(saveFolder + saveFilename, 'w+');
#	outputfile.write(MixedString);
