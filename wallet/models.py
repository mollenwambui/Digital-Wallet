from locale import currency
from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    adress=models.TextField(null=True)
    email=models.EmailField(null=True)
    phone_number=models.CharField(max_length=10,null=True)
    age=models.PositiveSmallIntegerField(null=True)
    GENDER_CHOICE = (("M","Male"),("F","Female"))
    gender=models.CharField(max_length=1,choices=GENDER_CHOICE,null=True)
    pin=models.CharField(max_length=4,null=True)
    id_number=models.CharField(max_length=10,null=True)
    nationality=models.CharField(max_length=20,null=True)
    occupation=models.CharField(max_length=10,null=True)
    signature=models.ImageField

class Currency(models.Model):
    amount=models.IntegerField()
    origin_country=models.CharField(max_length=10,null=True)

class Wallet(models.Model) :
    balance=models.IntegerField()
    # currency=models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='Wallet_currency')
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Wallet_customer')
    date_created=models.DateTimeField()
    pin=models.CharField(max_length=8,null=True)



class Account(models.Model) :
    account_type=models.CharField(max_length=15,null=True)
    balance=models.PositiveIntegerField()
    account_name=models.CharField(max_length=20,null=True)
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Account_wallet')


class Transaction(models.Model) :
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Transaction_wallet')
    transaction_amount=models.IntegerField()
    transaction_type=models.CharField(max_length=15,null=True)
    transaction_charge=models.IntegerField()
    transaction_date=models.DateTimeField(default=timezone.now)
    receipt=models.ForeignKey('Receipt',on_delete=models.CASCADE,related_name='Transaction_receipt')
    origin_account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Transaction_origin_account')
    destination_account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Transaction_destination_account')


class Card(models.Model)  :
    date_issued=models.DateTimeField(default=timezone.now)
    card_name=models.CharField(max_length=15,null=True)
    card_number=models.IntegerField()
    card_type=models.CharField(max_length=15,null=True)
    expiry_date=models.DateTimeField(default=timezone.now)
    card_status=models.CharField(max_length=15,null=True)
    security_code=models.IntegerField()
    signature=models.ImageField
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Card_wallet')
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Card_account')
    issuer=models.CharField(max_length=15,null=True)


class ThirdParty(models.Model)  :
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Thirdparty_account')
    name=models.CharField(max_length=15,null=True)
    thirdparty_id=models.IntegerField()
    phone_number=models.IntegerField()

class Notifications(models.Model) :
    notifications_id=models.IntegerField()
    name=models.CharField(max_length=15,null=True)
    status=models.CharField(max_length=15,null=True)
    date_and_time=models.DateTimeField(default=timezone.now)
    receipt=models.ForeignKey('Receipt',on_delete=models.CASCADE,related_name='Notifications_receipt')


class Receipt(models.Model):
    receipt_type=models.CharField(max_length=15,null=True)
    receipt_date=models.DateField(default=timezone.now)
    receipt_file=models.FileField()
    total_amount=models.IntegerField()
    # transaction=models.ForeignKey('Transaction',on_delete=models.CASCADE,related_name='Receipt_transaction')

class  Loan(models.Model):

    loan_number=models.IntegerField()
    loan_type=models.CharField(max_length=15,null=True)
    amount=models.IntegerField()
    date_and_time=models.DateTimeField(default=timezone.now)
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Loan_wallet')
    interest_rate=models.IntegerField()
    guarantor=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Loan_guarantor')
    pay_due_date=models.DateTimeField(default=timezone.now)
    loan_balance=models.IntegerField()

class Reward(models.Model):
    transaction=models.ForeignKey('Transaction',on_delete=models.CASCADE,related_name='Reward_transaction')
    date_and_time=models.DateTimeField(default=timezone.now)
    customer_id=models.IntegerField()
    GENDER_CHOICES=(("M","Male"),("F","Female"))
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
    bonus=models.IntegerField()





