# FOR THELEN:

run crawler.py to test the crawler. This will re-run the creating command of the index via whoosh (ix = create_in("indexdir", schema)). So it's best to delete the indexdir before running the crawler(at least that's what we always did).

flask server works as expected. Run
flask --app myapp.py run

# AiWebSearchEngine

create venv using:
python3 -m venv myenv

to activate venv use:
```source myenv/bin/activate```

to install requirements use:
```pip install -r requirements.txt```

test the crawler at:
https://vm009.rz.uos.de/crawl/

start webserver with:
flask --app myapp.py run

run crawler with:
python3 crawler.py