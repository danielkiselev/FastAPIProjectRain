import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE lineitems (
            lineitem_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price VARCHAR(255) NOT NULL,
            qty int NOT NULL,
            ID_INVOICE VARCHAR(255) NOT NULL
        )
            
        CREATE TABLE INVOICE (
            INVOICEID SERIAL PRIMARY KEY,
            PAYMENTSTATUS boolean,
            CLIENTID VARCHAR(255) NOT NULL,
            DESCRIPTION VARCHAR(255) NOT NULL,
            RECIPIENTEMAIL VARCHAR(255) NOT NULL,
        )

        """,
        """
        # CREATE TABLE part_drawings (
        #         part_id INTEGER PRIMARY KEY,
        #         file_extension VARCHAR(5) NOT NULL,
        #         drawing_data BYTEA NOT NULL,
        #         FOREIGN KEY (part_id)
        #         REFERENCES parts (part_id)
        #         ON UPDATE CASCADE ON DELETE CASCADE
        # )
        """,
        """
        # CREATE TABLE vendor_parts (
        #         vendor_id INTEGER NOT NULL,
        #         part_id INTEGER NOT NULL,
        #         PRIMARY KEY (vendor_id , part_id),
        #         FOREIGN KEY (vendor_id)
        #             REFERENCES vendors (vendor_id)
        #             ON UPDATE CASCADE ON DELETE CASCADE,
        #         FOREIGN KEY (part_id)
        #             REFERENCES parts (part_id)
        #             ON UPDATE CASCADE ON DELETE CASCADE
        # )
        # """)
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