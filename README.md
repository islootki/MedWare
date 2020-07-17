# General notes
- To verify the DB data a json file was created, `test_table.json` in `data_source` folder.
- The table was created with primary key as `CODE` column. 
- The query that generate the DB data can be found at  `sql_raw_data.sql`
- The database credentials are hard coded in the `consts` module
- Expected DB name is `test_1`
- Expected table name `test_table`
# Before execution 
Please install the following:
- pip install pytest
- pip install mysql-connector-python
# Test execution 
Please go to root dir (MedWare) of the project and run: 
- `pytest -q tests/tests.py` 
- The log files can be found at `log_dir`