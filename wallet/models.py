from locale import currency
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    adress=models.TextField
    email=models.EmailField
    phone_number=models.CharField
    age=models.PositiveSmallIntegerField

class Wallet(models.Model) :
    balance=models.IntegerField
    date_created=models.DateTimeField
    Customer=models.ForeignKey
    currency=models.ForeignKey
    pin=models.PositiveSmallIntegerField
    isActive=models.BooleanField


class Account(models.Model) :
    account_name=models.IntegerField
    balance=models.IntegerField
    Wallet=models.ForeignKey


class Transaction(models.Model) :
    transaction_code=models.CharField
    Wallet=models.ForeignKey
    transaction_amount=models.IntegerField
    transaction_number=models.IntegerField
    transaction_type=models.CharField
    date_time=models.DateTimeField
    origin_account=models.ForeignKey
    destination_account=models.ForeignKey
    isActive=models.BooleanField


class Card(models.Model)  :
    card_number=models.IntegerField
    card_name=models.CharField
    date_issued=models.DateTimeField
    card_type=models.CharField
    expiry_date=models.DateTimeField
    security_code=models.IntegerField
    Account=models.ForeignKey  
    issuer=models.CharField
    signature=models.ImageField


class ThirdParty(models.Model)  :
      name=models.CharField
      currency=models.CharField
      transaction_cost=models.IntegerField
      Account=models.ForeignKey

class Notifications(models.Model) :
     description=models.CharField
     title=models.CharField
     receipt=models.ForeignKey
     status=models.BooleanField
     date_time=models.DateTimeField


class Receipt(models.Model):
    receipt_type=models.CharField
    receipt_date=models.DateTimeField
    bill_number=models.IntegerField
    receipt_file=models.FileField
    transaction=models.IntegerField

class  Loan(models.Model):
    loan_id=models.IntegerField
    purpose=models.CharField
    amount=models.IntegerField
    name=models.CharField
    loan_status=models.CharField
    date_issued=models.DateTimeField
    Wallet=models.ForeignKey
    interest_rate=models.IntegerField
    payment_due_date=models.DateTimeField
    loan_balance=models.IntegerField
    guarantor=models.ForeignKey


class Reward(models.Model):
    receipient=models.ForeignKey
    date_of_reward=models.DateTimeField
    points=models.BigIntegerField
    transaction=models.ForeignKey






