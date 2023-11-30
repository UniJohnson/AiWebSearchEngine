from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.index import open_dir


from whoosh.index import create_in
from whoosh.fields import *

read_index = open_dir("indexdir")

# grab data from index

print("test")

with read_index.searcher() as searcher:
        # find entries with the words 'first' AND 'last'
        query = QueryParser("content", read_index.schema).parse("*")
        results = searcher.search(query)
        
        # print all results
        for r in results:
            print(r)
