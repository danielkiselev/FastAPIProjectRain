from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from .schemas import createlineitem,createinvoice,invoice,  lineitem,deleteEntry
app = FastAPI()
all_tasks: dict = {}
from config import load_config
from connect import connect
conf = load_config()
con = connect(config=conf)
from insert import insert_invoice, insert_line
from updateEntry import update_lineitem, update_invoice
from delete import delete_invoice, delete_lineitem


@app.post("/invoice", response_model=invoice)
def create_InvoiceService(invoiceData: createinvoice):

    id = insert_invoice(clientid=invoiceData.clientID, recipientemail=invoiceData.emailrecipient, description=invoiceData.description,)
    print(id)

    res = { "invoiceid": id,
                "emailrecipient": invoiceData.emailrecipient,
                "clientID": invoiceData.clientID,
                "description": invoiceData.description,
                "paymentStatus": False  }
    return res

@app.post("/lineitem", response_model=lineitem)
def create_lineitemService(lineitemdata: createlineitem):

    id = insert_line(lineitemdata = lineitemdata)
    print(id)

    if id is None:
        raise HTTPException(
            detail={'message': 'failed to create lineitem'},
            status_code=400
        )
    # all_tasks[task_slug] = task
    res = {     "lineitem_id": id,
    "name": lineitemdata.name,
    "price":  lineitemdata.price,
    "qty": lineitemdata.qty,
    "ID_INVOICE": lineitemdata.ID_INVOICE  }
    return res


@app.delete("/lineitem", response_model=lineitem)
def delete_lineitemService(uid: deleteEntry):
    print(uid)
    resQuery = delete_lineitem(uid)
    if resQuery is None:
        raise HTTPException(
            detail={'message': 'failed to delete lineitem'},
            status_code=400
        )
        # all_tasks[task_slug] = task
    print(resQuery)
    res = {"lineitem_id": resQuery[0],
           "name": resQuery[1],
           "price": resQuery[2],
           "qty": resQuery[3],
           "ID_INVOICE": resQuery[4]}
    return res

@app.delete("/invoice", response_model=invoice)
def delete_InvoiceService(uid: deleteEntry):

    print(uid)
    resQuery = delete_invoice(uid)
    if resQuery is None:
        raise HTTPException(
            detail={'message': 'failed to delete invoice'},
            status_code=400
        )
    print(resQuery)
    res = {"invoiceid": resQuery[0],
           "emailrecipient": resQuery[1],
           "clientID": resQuery[2],
           "description": resQuery[3],
           "paymentStatus": bool(resQuery[4])
           }
    return res

@app.put("/invoice", response_model=invoice)
def update_InvoiceService(invoiceData: invoice):

    resQuery = update_invoice(invoiceData)
    print(resQuery)

    if resQuery is None:
        raise HTTPException(
            detail={'message': 'failed to update invoice'},
            status_code=400
        )
    # all_tasks[task_slug] = task
    print(resQuery)
    res = {"invoiceid": resQuery[0],
           "emailrecipient": resQuery[1],
           "clientID": resQuery[2],
           "description": resQuery[3],
           "paymentStatus": bool(resQuery[4])
           }
    return res

@app.put("/lineitem", response_model=lineitem)
def update_lineitemService(lineitemdata: lineitem):

    resQuery = update_lineitem(lineitemdata = lineitemdata)

    if resQuery is None:
        raise HTTPException(
            detail={'message': 'failed to update lineitem'},
            status_code=400
        )
    # all_tasks[task_slug] = task
    print(resQuery)
    res = {"lineitem_id":resQuery[0],
           "name": resQuery[1],
           "price": resQuery[2],
           "qty":resQuery[3],
           "ID_INVOICE":resQuery[4] }
    return res



@app.get("/")
def home():
    return "Welcome to our TODO application. Add /docs to the current URL to visit our docs page"
