import psycopg2

from config import load_config



def delete_lineitem(uid):
    sql_query = """
                DELETE
                FROM lineitems
                WHERE "lineitem_id" = %s RETURNING *; \
                """
    config = load_config()
    deleted_row = None
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql_query, (uid.uid,))  # Pass ID as a tuple

                # --- 4. Fetch the returned (deleted) row ---
                deleted_row = cur.fetchone()
                if deleted_row:
                    print("\n--- Successfully deleted the following row ---")
                    # The deleted_row is a tuple of the deleted data
                    print(f"  Line Item ID: {deleted_row[0]}")
                    print(f"  Name: {deleted_row[1]}")
                    print(f"  Price: ${deleted_row[2]}")
                else:
                    # This will occur if the ID didn't exist in the table
                    print(f"\nNo row found with lineitem_id: {uid}. Nothing deleted.")

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return deleted_row


def delete_invoice(uid):
    sql_query = """
                DELETE
                FROM invoice
                WHERE "invoiceid" = %s RETURNING *; \
                """
    config = load_config()
    deleted_row = None
    try:
        with  (psycopg2.connect(**config) as conn):
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql_query, (uid.uid,))
                deleted_row = cur.fetchone()
                if deleted_row:
                    print("\n--- Successfully deleted the following row ---")
                    # The deleted_row is a tuple of the deleted datapaymentstatus, clientid, description, recipientemail
                    print(f"  deleted invoice ID: {deleted_row[0]}")
                    print(f"  paymentstatus: {deleted_row[1]}")
                    print(f"  clientid: ${deleted_row[2]}")
                else:
                    # This will occur if the ID didn't exist in the table
                    print(f"\nNo row found with lineitem_id: {uid}. Nothing deleted.")
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return deleted_row
