# Slick-pay
![Logo](https://camo.githubusercontent.com/fa6dcd1937e50537d858c75f7fb2c0b8ade213c3fc65ceb762ce8fadbfa3ff5a/68747470733a2f2f617a696d7574627363656e7465722e636f6d2f6c6f676f732f736c69636b2d7061792e706e67)
# Description
#### _Python package for Slick-Pay Transfer API implementation._
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [How to use?](#howtouse?)
- [More help](#Morehelp)

# Prerequisites
- Python 3
- requests~=2.27.0
- python-dotenv~=0.21.1
# Installation
Just run this command line :
```python
  pip install slick-pay==0.3

```
# Configuration
In order to use our API, you will need to :
#### 1. Create an account
Visite [our website ](https://slick-pay.com/) and create an account. If you are merchant you have to add your satim information like username and password
#### 2. Get api's key
After logging in, from your dashboard, you will able to get your PUBLIC_KEY.
#### 3. Configure through environment variables
Create a .env file and inside your .env file create a variable like this:
```python
  public_key= your_public_key
  sandbox= True or False
```
# How to use?
## Concerning merchant account
## InvoiceTransferMerchant
### Create Invoice
```python
from slickpay import InvoiceTransferMerchant
    invoiceMerchant = InvoiceTransferMerchant()
    data = 
    {
        'amount': 10000,
        'name': "Lorem Ipsum",
        'phone': "000000000",
        'address': "Lorem Ipsum Address",
        'url': "https://my-website.com/thank-you-page",
        'items': [
            {
                "name": "Seller product",
                "price": 5000,
                "quantity": 2
            }
        ]
    }
    res = invoiceMerchant.createInvoice(data)
    return res
```
### Invoice Details
```python
    res = invoiceMerchant.invoiceDetail(id)
    return res
```
### List Invoice
```python
    res = invoiceMerchant.listInvoice(offset,  page)
    return res
```
### Update Invoice
```python
    res = invoiceMerchant.updateInvoice(id, data)
    return res
```
### Delete Invoice
```python
    res = invoiceMerchant.deleteInvoice(id, data)
    return res
```
## Concerning User account:
## Account
### Create
```python
from slickpay import Account
    userAccount = Account()
    data = {
        "title"    : "Lorem Ipsum",
        "lastname" : "Lorem",
        "firstname": "Ipsum",
        "address"  : "Lorem Ipsum Address",
        "rib"      : "12345678912345678900"
    }
    res = userAccount.create(data)
    return res
```
### Account Details
```python
    res = userAccount.accountDetails(id)
    return res
```
### Account list
```python
    res = userAccount.list(offset, page)
    return res
```
### Account update
```python
    res = userAccount.update(id, data)
    return res
```
### Account delete
```python
    res = userAccount.delete(id)
    return res
```
## Contact
### Create Contact
```python
from slickpay import Contact
    userContact = Contact()
    data = {
        "title"    : "Lorem Ipsum",
        "lastname" : "Lorem",
        "firstname": "Ipsum",
        "email"    : "lorem@ipsum.com",
        "address"  : "Lorem Ipsum Address",
        "rib"      : "12345678912345678900"
    }
    res = userContact.createContact(data)
    return res
```
### Contact detail
```python
    res = userContact.contactDetail(id)
    return res
```
### Contact list
```python
    res = userContact.listContact(offset, page)
    return res
```
### Contact update
```python
    res = userContact.updateContact(id, data)
    return res
```
### Contact delete
```python
    res = userContact.deleteContact(id)
    return res
```
## Transfer
### Calculate Commission
```python
from slickpay import Transfer
    userTransfer = Transfer()
    res=userTransfer.calculateCommission(amount)
    return res
```
### Create Transfer
```python
     data = {
        'amount' : 1000,
        'uuid'   : "37990d08-fc51-4c32-ad40-1552d13c00d1",
        'url'    : "https://my-website.com/thank-you-page",
    }
    res = userTransfer.createPayment(data)
    return res
```
### Transfer detail
```python
    res = userTransfer.paymentDetail(id)
    return res
```
### Transfer list
```python
    res = userTransfer.listTransfer(offset, page)
    return res
```
### Transfer update
```python
    res = userTransfer.updateTransfer(id, data)
    return res
```
### Transfer delete
```python
    res = userTransfer.deleteTransfer(id)
    return res
```
## PaymentAggregation
### Calculate Commission
```python
from slickpay import PaymentAggregation
    userPaymentAggregation = PaymentAggregation()
    data = {
        "type": "percentage",
        "total": 10000,
        "contacts": [
            {
                "uuid": "864efcd3-9fef-4da5-67ec-bc28fd7e719b",
                "amount": 50
            },
            {
                "uuid": "f23bde3f-aac9-4dfc-7e06-5bf02e7f5967",
                "amount": 50
            }
        ]
    }
    res=userPaymentAggregation.commission(data)
    return res
```
### Create PaymentAggregation
```python
     data = {
        "url"     : "https://my-website.com/thank-you-page",
        "type"    : "percentage",
        "total"   : 10000,
        "contacts": [
            {
                "uuid": "864efcd3-9fef-4da5-67ec-bc28fd7e719b",
                "amount": 50
            },
            {
                "uuid": "f23bde3f-aac9-4dfc-7e06-5bf02e7f5967",
                "amount": 50
            }
        ]
    }
    res = userPaymentAggregation.create(data)
    return res
```
### PaymentAggregation detail
```python
    res = userPaymentAggregation.details(id)
    return res
```
### PaymentAggregation list
```python
    res = userPaymentAggregation.list(offset, page)
    return res
```
### PaymentAggregation update
```python
    data = {
        "url"     : "https://my-website.com/thank-you-page",
        "type"    : "percentage",
        "total"   : 20000,
        "contacts": [
            {
                "uuid": "864efcd3-9fef-4da5-67ec-bc28fd7e719b",
                "amount": 50
            },
            {
                "uuid": "f23bde3f-aac9-4dfc-7e06-5bf02e7f5967",
                "amount": 50
            }
        ]
    }
    res = userPaymentAggregation.update(id, data)
    return res
```
### PaymentAggregation delete
```python
    res = userPaymentAggregation.delete(id)
    return res
```
## InvoiceTransfer
### Calculate Commission
```python
from slickpay import InvoiceTransfer
    userInvoiceTransfer = InvoiceTransfer()
    res=userInvoiceTransfer.calculateCommissionInvoice(amount)
    return res
```
### Create InvoiceTransfer
```python
    data = {
        'amount' : 10000,
        'uuid'   : "37990d08-fc51-4c32-ad40-1552d13c00d1",
        'url'    : "https://my-website.com/thank-you-page",
        'items'  : [
            {
                "name": "Seller product",
                "price": 5000,
                "quantity": 2
            }
        ]
    }
    res = userInvoiceTransfer.createInvoice(data)
    return res
```
### InvoiceTransfer detail
```python
    res = userInvoiceTransfer.InvoiceDetail(id)
    return res
```
### InvoiceTransfer list
```python
    res = userInvoiceTransfer.listInvoice(offset, page)
    return res
```
### InvoiceTransfer update
```python
    data = {
        'amount' : 1000,
        'uuid'   : "37990d08-fc51-4c32-ad40-1552d13c00d1",
        'url'    : "https://my-website.com/thank-you-page",
    }
    res = userInvoiceTransfer.updateInvoice(id, data)
    return res
```
### InvoiceTransfer delete
```python
    res = userInvoiceTransfer.deleteInvoice(id)
    return res
```
# More help
- [Slick-Pay website](https://slick-pay.com/)
- [devapi-slick-pay](https://www.devapi.slick-pay.com/)