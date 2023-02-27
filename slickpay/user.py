import os

import requests

from dotenv import load_dotenv

load_dotenv()


class Account:

    def create(self, data):
        print(self)
        if os.environ["sandbox"]:
            url = 'https://www.devapi.slick-pay.com/api/v2/users/accounts'
        else:
            url = 'https://www.prodapi.slick-pay.com/api/v2/users/accounts'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.post(url, headers=headers, data=data)
        body = res.json()
        return body

    def update(self, uid, data):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/accounts/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/accounts/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}

        res = requests.put(url, headers=headers, json=data)

        return res.json()

    def list(self, offset, page):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/accounts?offset={int(offset)}&page={int(page)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/accounts?offset={int(offset)}&page={int(page)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.json()

    def accountDetails(self, uid):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/accounts/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/accounts/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.json()

    def delete(self, uid):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/accounts/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/accounts/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.delete(url, headers=headers)

        return res.json()


class Contact:

    def createContact(self, data):
        print(self)
        if os.environ["sandbox"]:
            url = 'https://www.devapi.slick-pay.com/api/v2/users/contacts'
        else:
            url = 'https://www.prodapi.slick-pay.com/api/v2/users/contacts'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.post(url, headers=headers, json=data)
        body = res.json()
        return body

    def contactDetail(self, uid):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/contacts/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/contacts/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.json()

    def listContact(self, offset, page):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/contacts?offset={int(offset)}&page={int(page)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/contacts?offset={int(offset)}&page={int(page)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.json()

    def updateContact(self, data, uid):
        print(self)
        if os.environ["sandbox"]:
            url = 'https://www.devapi.slick-pay.com/api/v2/users/contacts/'+str(uid)
        else:
            url = 'https://www.prodapi.slick-pay.com/api/v2/users/contacts/'+str(uid)
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.put(url, headers=headers, data=data)

        return res.json()

    def deleteContact(self, uid):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/contacts/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/contacts/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.delete(url, headers=headers)

        return res.json()


class Transfer:

    def calculateCommission(self, amount):
        print(self)
        if os.environ["sandbox"]:
            url = 'https://www.devapi.slick-pay.com/api/v2/users/transfers/commission'
        else:
            url = 'https://www.prodapi.slick-pay.com/api/v2/users/transfers/commission'

        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        data = {
            'amount': amount
        }
        res = requests.post(url, headers=headers, data=data)
        return res.content

    def createPayment(self, data):
        print(self)
        if os.environ["sandbox"]:
            url = 'https://www.devapi.slick-pay.com/api/v2/users/transfers'
        else:
            url = 'https://www.prodapi.slick-pay.com/api/v2/users/transfers'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.post(url, headers=headers, json=data)
        # print(res)
        body = res.json()
        return body
        # return res

    def paymentDetail(self, uid):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/transfers/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/transfers/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.json()

    def listTransfer(self, offset, page):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/transfers?offset={int(offset)}&page={int(page)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/transfers?offset={int(offset)}&page={int(page)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.json()

    def updateTransfer(self, data, uid):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/transfers/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/transfers/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.put(url, headers=headers, json=data)

        return res.json()

    def deleteTransfer(self, uid):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/transfers/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/transfers/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.delete(url, headers=headers)

        return res.json()


class PaymentAggregation:

    def commission(self, data):
        print(self)
        if os.environ["sandbox"]:
            url = 'https://www.devapi.slick-pay.com/api/v2/users/aggregations/commission'
        else:
            url = 'https://www.prodapi.slick-pay.com/api/v2/users/aggregations/commission'

        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}

        res = requests.post(url, headers=headers, json=data)
        return res.content

    def create(self, data):
        print(self)
        if os.environ["sandbox"]:
            url = 'https://www.devapi.slick-pay.com/api/v2/users/aggregations'
        else:
            url = 'https://www.prodapi.slick-pay.com/api/v2/users/aggregations'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.post(url, headers=headers, json=data)
        body = res.json()
        return body

    def details(self, uid):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/aggregations/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/aggregations/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.json()

    def list(self, offset, page):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/aggregations?offset={int(offset)}&page={int(page)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/aggregations?offset={int(offset)}&page={int(page)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.json()

    def update(self, data, uid):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/aggregations/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/aggregations/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.put(url, headers=headers, json=data)
        body = res.json()
        return body

    def delete(self, uid):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/aggregations/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/aggregations/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.delete(url, headers=headers)
        body = res.json()
        return body


class InvoiceTransfer:

    def calculateCommissionInvoice(self, amount):
        print(self)
        if os.environ["sandbox"]:
            url = 'https://www.devapi.slick-pay.com/api/v2/users/invoices/commission'
        else:
            url = 'https://www.prodapi.slick-pay.com/api/v2/users/invoices/commission'

        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        data = {
            'amount': amount
        }
        res = requests.post(url, headers=headers, data=data)
        return res.content

    def createInvoice(self, data):
        print(self)
        if os.environ["sandbox"]:
            url = 'https://www.devapi.slick-pay.com/api/v2/users/invoices'
        else:
            url = 'https://www.prodapi.slick-pay.com/api/v2/users/invoices'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.post(url, headers=headers, json=data)
        body = res.json()
        return body

    def InvoiceDetail(self, uid):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/invoices/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/invoices/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.json()

    def listInvoice(self, offset, page):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/invoices?offset={int(offset)}&page={int(page)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/invoices?offset={int(offset)}&page={int(page)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.json()

    def updateInvoice(self, data, uid):
        print(self)
        if os.environ["sandbox"]:
            url = 'https://www.devapi.slick-pay.com/api/v2/users/invoices/'+str(uid)
        else:
            url = 'https://www.prodapi.slick-pay.com/api/v2/users/invoices/'+str(uid)
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.put(url, headers=headers, json=data)

        return res.json()

    def deleteInvoice(self, uid):
        print(self)
        if os.environ["sandbox"]:
            url = f'https://www.devapi.slick-pay.com/api/v2/users/invoices/{int(uid)}'
        else:
            url = f'https://www.prodapi.slick-pay.com/api/v2/users/invoices/{int(uid)}'
        headers = {"Authorization": f'{str(os.environ["public_key"])}', "Accept": "application/json"}
        res = requests.delete(url, headers=headers)

        return res.json()
