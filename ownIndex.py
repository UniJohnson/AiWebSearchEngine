from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.index import open_dir


from whoosh.index import create_in
from whoosh.fields import *

#init whoosh first with a schema
schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True), url=ID(stored=True))
ix = create_in("indexdir", schema)
writer = ix.writer()


def add_document(param_title, param_content, param_url):
    print("added document to index. Still need to write the commit")
    writer.add_document(title=u"" + param_title, content=u"" + param_content, url=u"" + param_url)

def commit_writer():
    writer.commit()
