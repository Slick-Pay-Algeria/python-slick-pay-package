import os

import requests
from dotenv import load_dotenv

load_dotenv()


class InvoiceTransferMerchant:

    def createInvoice(self, data):
        print(self)
        if os.environ["sandbox"]:
            url = 'https://www.devapi.slick-pay.com/api/v2/merchants/invoices'
        else:
            url = 'https://www.prodapi.slick-pay.com/api/v2/merchants/invoices'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.post(url, headers=headers, json=data)
        body = res.json()
        return body

    def invoiceDetail(self, uid):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/merchants/invoices/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/merchants/invoices/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.content

    def listInvoice(self, offset, page):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/merchants/invoices?offset={int(offset)}&page={int(page)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/merchants/invoices?offset={int(offset)}&page={int(page)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.content

    def updateInvoice(self, data, uid):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/merchants/invoices/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/merchants/invoices/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.put(url, headers=headers, json=data)

        return res.json()

    def deleteInvoice(self, uid):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/merchants/invoices/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/merchants/invoices/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.delete(url, headers=headers)

        return res.json()
