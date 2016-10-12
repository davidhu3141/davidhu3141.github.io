import sys
sys.path.append('./module')

import json
import bytify
import pageGen
import articleCmp
import sys, getopt
from os import walk
from os import makedirs
from os import path

def main(argv):

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

	# commandline args fetch
	try:
		opts, args = getopt.getopt(argv, "sgn", ["status", "generate", "nongenerated"])
	except getopt.GetoptError:
		print 'anthoGen.py -s --status'
		print 'anthoGen.py -n --nongenerated'
		sys.exit(2)

	# jobs
	for opt, arg in opts:
		if opt in ("-s", "--status"):
		    
		    print "nothing."
		    sys.exit()
		
		elif opt in ("-g", "--generate"):
		    
			# MODULE: article list generate
			articleListString = pageGen.articleListGen(fromFolder, saveFolder, webResourceRoot)

			# MODULE: HTML content generate
			pageGen.articleGen(fromFolder, saveFolder, webResourceRoot, articleListString, templeteString)

			# MODULE: Index page generate
			indexTempletePath = confJson['indexTempletePath']
			pageGen.indexPageGen(indexTempletePath, articleListString)
			sys.exit()

		elif opt in ("-n", "--nongenerated"):
		
			src = articleCmp.fileStruct(fromFolder)
			dst = articleCmp.fileStruct(saveFolder)
			notgencat, notgenart = articleCmp.fileStructCmp(src, dst)

			print ''
			print '[not generated categories:]'
			print notgencat
			print ''
			print '[not generated articles:]'
			print notgenart

			sys.exit()

	print 'Nothing is done.'

if __name__ == "__main__":
	main(sys.argv[1:])

