from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.index import open_dir


from whoosh.index import create_in
from whoosh.fields import *

#init whoosh first with a schema
schema = Schema(title=TEXT(stored=True), content=TEXT)
ix = create_in("indexdir", schema)
writer = ix.writer()

read_index = open_dir("indexdir")

# grab data from index
def get_data_from_index(search_term):

    with read_index.searcher() as searcher:
        # find entries with the words 'first' AND 'last'
        query = QueryParser("content", read_index.schema).parse("*")
        results = searcher.search(query)
        
        # print all results
        for r in results:
            print(r)

        return results

def add_document(param_title, param_content):
    print("added document to index. Still need to write the commit")
    writer.add_document(title=u"" + param_title, content=u"" + param_content)
    #writer.add_document(title=u"First document", content=u"This is the first document we've added!")
    #writer.add_document(title=u"Second document", content=u"The second one is even more interesting!")
    writer.add_document(title=u"Songtext", content=u"Music was my first love and it will be the last")

def commit_writer():
    writer.commit()
