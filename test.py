import search
from search import ScholarSearch
'''
pub = "attention is all you need"
#tmp = next(scholarly.search_pubs_query(pub)).bib
tmp = ScholarSearch()
tmp.result = tmp.search_pubs()

print(tmp.result[0]['title'])
'''
import pybtex.database

print('pybtex version:', pybtex.__version__)

bib_data = pybtex.database.parse_file("finalbib.bib", bib_format='bibtex')
#bib_data.to_file('finalbib.bib', bib_format='bibtex')
print(bib_data.entries['bahdanau2014neural'])
print(bib_data.to_string('bibtex'))
#bib_data.entries['bahdanau2014neural'].to_file('testbib.bib', bib_format='bibtex')