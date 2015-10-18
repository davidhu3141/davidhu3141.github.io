# coding=utf-8

import sys
import urllib2
import json

def byteify(input):
	if isinstance(input, dict):
		return {byteify(key):byteify(value) for key,value in input.iteritems()}
	elif isinstance(input, list):
		return [byteify(element) for element in input]
	elif isinstance(input, unicode):
		return input.encode('utf-8')
	else:
	        return input

def loadAllContent (dest) :
	try :
		headers = {
			'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
		}
		req = urllib2.Request(
			url = dest,
			headers = headers
		)
		return urllib2.urlopen(req).read()
	except:
		return None

# templete file
templeteFile = open('templete.html', 'r')
templeteString = templeteFile.read()

# json file
jsonArticleListFile = open('articlelist.json', 'r')
jsonArticleListString = jsonArticleListFile.read()
jsonArticleList = json.loads(jsonArticleListString)
jsonArticleList = byteify(jsonArticleList)

articles = jsonArticleList['articles']
initialPath = jsonArticleList['initialpath']
particularPath = articles[1]['path']
saveFolder = 'tempHTML/'
saveFilename = particularPath

articleBody = loadAllContent(initialPath + particularPath)
MixedString = templeteString.replace('<!--@Article-->', articleBody).replace('<!--@RootPath-->', 'davidhu3141.github.io');

# save file
outputfile = open(saveFolder + saveFilename, 'w+');
outputfile.write(MixedString);
