from pydantic import BaseModel


#             INVOICEID SERIAL PRIMARY KEY,
#             PAYMENTSTATUS boolean,
#             CLIENTID VARCHAR(255) NOT NULL,
#             DESCRIPTION VARCHAR(255) NOT NULL,
#             RECIPIENTEMAIL VARCHAR(255) NOT NULL,


class createinvoice(BaseModel):
    emailrecipient: str
    clientID: str
    description: str
    paymentStatus: bool

    class Config:
        schema_extra = {
            "example": {
                "emailrecipient": "<EMAIL>",
                "clientID": "<clientID>",
                "description": "text",
                "paymentStatus": False
            }
        }


class invoice(BaseModel):
    invoiceid: str
    emailrecipient: str
    clientID: str
    description: str
    paymentStatus: bool

    class Config:
        schema_extra = {
            "example": {
                "invoiceid": "<invoiceID>",
                "emailrecipient": "<EMAIL>",
                "clientID": "<clientID>",
                "description": "text",
                "paymentStatus": False
            }
        }


class createlineitem(BaseModel):
    name: str
    price: str
    qty: str
    ID_INVOICE: str

    class Config:
        schema_extra = {
            "example": {
                "name": "<name>",
                "price": "<price",
                "qty": "<qty>",
                "ID_INVOICE": "1"
            }
        }


class lineitem(BaseModel):
    lineitem_id: str
    name: str
    price: str
    qty: str
    ID_INVOICE: str

    class Config:
        schema_extra = {
            "example": {
                "lineitem_id": "<lineitemUID>",
                "name": "<name>",
                "price": "<price",
                "qty": "<qty>",
                "ID_INVOICE": "1"
            }
        }


class deleteEntry(BaseModel):
    uid: str

    class Config:
        schema_extra = {
            "example": {
                "uid": "<ID for lineitem or Invoice>"
            }
        }

#            lineitem_id SERIAL PRIMARY KEY,
#             name VARCHAR(255) NOT NULL,
#             price VARCHAR(255) NOT NULL,
#             qty int NOT NULL,
#             ID_INVOICE VARCHAR(255) NOT NULL

# class TodoTaskModel(BaseModel):
#     slug: str
#     title: str
#     description: str
#     status: str
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "slug": "test-task",
#                 "title": "Test task",
#                 "description": "Just some test task",
#                 "status": "In progress"
#             }
#         }
