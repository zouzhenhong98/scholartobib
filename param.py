import scholar
import pybtex
from pybtex.database import BibliographyData, Entry
#import bibtexparser
#from bibtexparser.bwriter import BibTexWriter
#from bibtexparser.bibdatabase import Bibdatabase
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

file_r = r"./read_list.txt"
file_w = r"./write_list.txt"
file_b = r"./mybib.bib"