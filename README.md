# Wiktionary-Tree
An object structure of Wiktionary, used to extract specific data

```.
.
|____playground.py               <- Updated
|____.gitignore
|____pytest.ini
|____clarity-data
| |____reagentkit_data.json       <- NEW
| |____automation_data.json       <- NEW
| |____researcher_data.json
| |____project_data.json
| |____container_data.json
| |____process_data.json
| |____artifact_data.json
| |____instrument_data.json       <- NEW
| |____reagentlot_data.json       <- NEW
| |____objects_statistics.txt     <- Updated
| |____sample_data.json
|____.pytest_cache
| |____.gitignore
| |____CACHEDIR.TAG
| |____README.md
| |____v
| | |____cache
| | | |____lastfailed
| | | |____stepwise
| | | |____nodeids
|____tests
| |____test_udfconfig.py          <- NEW
| |____test_workflow.py           <- NEW
| |______init__.py
| |____test_researcher.py
| |____test_container.py
| |____test_instrument.py         <- NEW
| |____test_automation.py         <- NEW
| |____test_process.py
| |____test_samplehistory.py      <- NEW
| |____fixtures
| | |____instrument_fixtures.py   <- NEW
| | |____reagentlot_fixtures.py   <- NEW
| | |____sample_fixtures.py
| | |____samplehistory_fixtures.py<- NEW
| | |____researcher_fixtures.py
| | |____automation_fixtures.py   <- NEW
| | |____container_fixtures.py
| | |____process_fixtures.py
| | |____file_fixtures.py
| | |____reagentkit_fixtures.py   <- NEW
| | |____project_fixtures.py
| |____test_protocol.py           <- NEW
| |____test_reagentkit.py         <- NEW
| |____test_sample.py
| |____test_file.py
| |____conftest.py                <- Updated
| |____test_project.py
| |____test_reagentlot.py         <- NEW
|____conftest.py
|____README.md
``` 
