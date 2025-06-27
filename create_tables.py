import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """CREATE TABLE lineitems (
            lineitem_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price VARCHAR(255) NOT NULL,
            qty int NOT NULL,
            ID_INVOICE VARCHAR(255) NOT NULL
        )""",
            
        """CREATE TABLE INVOICE (
            INVOICEID SERIAL PRIMARY KEY,
            PAYMENTSTATUS boolean,
            CLIENTID VARCHAR(255) NOT NULL,
            DESCRIPTION VARCHAR(255) NOT NULL,
            RECIPIENTEMAIL VARCHAR(255) NOT NULL
        )"""
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    create_tables()