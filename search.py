from param import *

class ScholarSearch(object):
	"""
	mode: function
	'author': return info of enquire author and write them in 'author_info.txt'
	'pub': return info of enquire publication and write them in 'mybib.bib'
	'keyword': return info of enquire keyword, top 10 related authors and write them in 'key_author.txt'
	"""
	def __init__(self):
		self.file_r = file_r
		self.file_w = file_w
		self.file_b = file_b
		self.query = self.read_file()	# store enquire words query
		self.result = []

	def read_file(self):
		logging.info("...read from files...")
		with open(self.file_r) as f:
			content = f.readlines()
		logging.info('loaded names')
		logging.info(content)
		return [c.strip() for c in content]

	def write_txt(self):
		logging.info("...write to txt files...")
		with open(self.file_w, 'w') as f:
			for item in self.result:
				f.write("%s\n" % item)

	# write info to mybib.bib
	def write_bib(self):
		logging.info("...write to bib files...")
		'''using package 'bibtexparser'
		db = bibDatabase()
		with open(self.file_b, 'w') as f:
			for item in self.result:
				db.entries = [
				{'journal': item['journal'],
			     'abstract': item['abstract'],
			     'title': item['title'],
			     'author': item['author']
			    }]
		'''
		bib_data = BibliographyData({
			self.result[0]['author']
			:Entry('article',[
				('author', self.result[0]['author']),
				('title', self.result[0]['title']),
				('abstract', self.result[0]['abstract']),
				('url', self.result[0]['url']),
				('eprint', self.result[0]['eprint']),
				#('journal', self.result[0]['journal']),
				#('year', self.result[0]['year']),
				]),
			})
		bib_data.to_file('test.bib', bib_format='bibtex')
		logging.info(bib_data.to_string('bibtex'))

	def search_author(self):
		logging.info("...return author info...")
		self.result = [next(scholar.search_author(name)) for name in self.query]

	def search_pubs(self): 
		logging.info("...return publication info...")
		self.result = [next(scholar.search_pubs_query(pub)).bib for pub in self.query]

	def search_keyword(self):
		logging.info("...return related authors...")
		self.result = [next(scholar.search_keyword(keyword)) for keyword in self.query]


if __name__ == "__main__":
	logger.info("...start processing...")
	search = ScholarSearch()
	
	mode = 'pub'
	if mode == 'author':
		search.search_author()
		search.write_txt()
	elif mode == 'pub':
		search.search_pubs()
		search.write_bib()
		#print(search.result[0])
	elif mode == 'keyword':
		search.search_keyword()
		search.write_txt()
	else:			
		print("error mode")