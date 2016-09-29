from os import walk

# article list pregenerate
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
