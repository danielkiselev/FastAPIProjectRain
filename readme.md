edit the database.ini file pointing to your psql server database. 

install dependencies `pip install -r requirements.txt`

create_tables.py 

run the `create_tables.py` file to create empty tables for the app.

`python create_tables.py`

run the application
`uvicorn app.main:app --reload`

access the swagger ui where you can easily call the create, update, and delete requests by navigating to

`localhost:8000/docs` 
