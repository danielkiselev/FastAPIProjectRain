import psycopg2

from config import load_config


# INSERT INTO public.invoice

# (invoiceid, paymentstatus, clientid, description, recipientemail)
# VALUES(nextval('invoice_invoiceid_seq'::regclass), false, '', '', '');

def update_lineitem(lineitemdata):
    if not validInvoiceCheck(lineitemdata.ID_INVOICE):
        return None
    sql_query = """
                UPDATE lineitems
                SET "name"=%s,
                    price=%s,
                    qty=%s,
                    id_invoice=%s
                WHERE lineitem_id = %s
                RETURNING * \
                """

    config = load_config()
    row = None
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql_query,
                            (lineitemdata.name, lineitemdata.price, lineitemdata.qty, lineitemdata.ID_INVOICE,
                             lineitemdata.lineitem_id))
                row = cur.fetchone()

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return row


def update_invoice(invoicedata):
    sql_query = """
                UPDATE invoice
                SET "paymentstatus"=%s,
                    clientid=%s,
                    description=%s,
                    recipientemail=%s
                WHERE invoiceid = %s
                RETURNING * \
                """

    config = load_config()
    row = None
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql_query, (invoicedata.paymentStatus, invoicedata.clientID, invoicedata.paymentStatus,
                                        invoicedata.emailrecipient, invoicedata.invoiceid))
                row = cur.fetchone()

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return row


def validInvoiceCheck(id):
    sql = """SELECT *
             FROM invoice
             WHERE invoiceid = %s;"""
    config = load_config()
    exists = False
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (id,))
                rows = cur.fetchone()
                if rows:
                    exists = True
                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return exists

# CREATE TABLE lineitems (
#             lineitem_id SERIAL PRIMARY KEY,
#             name VARCHAR(255) NOT NULL,
#             price VARCHAR(255) NOT NULL,
#             qty int NOT NULL,
#             ID_INVOICE VARCHAR(255) NOT NULL
#         )


#             INVOICEID SERIAL PRIMARY KEY,
#             PAYMENTSTATUS boolean,
#             CLIENTID VARCHAR(255) NOT NULL,
#             DESCRIPTION VARCHAR(255) NOT NULL,
#             RECIPIENTEMAIL VARCHAR(255) NOT NULL,


# def insert_vendor(vendor_name):
#     """ Insert a new vendor into the vendors table """
#     sql = """INSERT INTO invoice(vendor_name)
#              VALUES(%s) RETURNING vendor_id;"""
#     vendor_id = None
#     config = load_config()
#     try:
#         with  psycopg2.connect(**config) as conn:
#             with  conn.cursor() as cur:
#                 # execute the INSERT statement
#                 cur.execute(sql, (vendor_name,))
#                 # get the generated id back
#                 rows = cur.fetchone()
#                 if rows:
#                     vendor_id = rows[0]
#                 # commit the changes to the database
#                 conn.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         return vendor_id


# def delete_vendor(vendor_name):
#     """ Insert a new vendor into the vendors table """
#     sql = """INSERT INTO users(vendor_name)
#              VALUES(%s) RETURNING vendor_id;"""
#     vendor_id = None
#     config = load_config()
#     try:
#         with  psycopg2.connect(**config) as conn:
#             with  conn.cursor() as cur:
#                 # execute the INSERT statement
#                 cur.execute(sql, (vendor_name,))
#                 # get the generated id back
#                 rows = cur.fetchone()
#                 if rows:
#                     vendor_id = rows[0]
#                 # commit the changes to the database
#                 conn.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         return vendor_id
