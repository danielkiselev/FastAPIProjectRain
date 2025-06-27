import psycopg2

from config import load_config


# INSERT INTO public.invoice

# (invoiceid, paymentstatus, clientid, description, recipientemail)
# VALUES(nextval('invoice_invoiceid_seq'::regclass), false, '', '', '');

def insert_invoice(clientid, description, recipientemail):
    data = (False, clientid, description, recipientemail)
    """ Insert a new vendor into the vendors table """
    sql = """INSERT INTO invoice
                 (paymentstatus, clientid, description, recipientemail)
             VALUES (%s, %s, %s, %s)RETURNING invoiceid;"""
    invoiceid = None
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, data)
                # get the generated id back
                rows = cur.fetchone()
                if rows:
                    invoiceid = rows[0]
                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return invoiceid


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


# INSERT INTO public.lineitems (lineitem_id, "name", price, qty, id_invoice) VALUES(nextval('lineitems_lineitem_id_seq'::regclass), '', '', 0, '');
def insert_line(lineitemdata):
    data = (lineitemdata.name, lineitemdata.price, lineitemdata.qty, lineitemdata.ID_INVOICE)
    if not validInvoiceCheck(lineitemdata.ID_INVOICE):
        return None
    """ Insert a new vendor into the vendors table """
    sql = """INSERT INTO lineitems
                 ("name", price, qty, id_invoice)
             VALUES (%s, %s, %s, %s)RETURNING lineitem_id;"""
    lineitem_id = None
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, data)
                # get the generated id back
                rows = cur.fetchone()
                if rows:
                    lineitem_id = rows[0]
                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return lineitem_id

