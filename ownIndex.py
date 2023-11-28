from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser


#init whoosh first with a schema
schema = Schema(title=TEXT(stored=True), content=TEXT)
ix = create_in("indexdir", schema)
writer = ix.writer()

# grab data from index
def get_data_from_index(search_term):
    with ix.searcher() as searcher:
        # find entries with the words 'first' AND 'last'
        query = QueryParser("content", ix.schema).parse(search_term)
        results = searcher.search(query)
        
        # print all results
        for r in results:
            print(r)

        return results

def commit_writer():
    writer.commit()

def add_document(param_title, param_content):
    print("added document to index. Still need to write the commit")
    #writer.add_document(title=param_title, content=param_content)
    writer.add_document(title=u"First document", content=u"This is the first document we've added!")


# test function for printing the entire index
def print_index():
    with ix.searcher() as searcher:
        # find entries with the words 'first' AND 'last'
        query = QueryParser("content", ix.schema).parse("*")
        results = searcher.search(query)
        
        # print all results
        for r in results:
            print(r)

        return results