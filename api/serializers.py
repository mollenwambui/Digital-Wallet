from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from wallet.models import Account, Card, Customer, Loan, Notifications, Receipt, Transaction, Wallet


class Customer_serializers(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=("first_name","email","age")


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        fields=("balance","customer","date_created","pin") 

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=("account_type","account_name","balance","wallet")     

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Card
        fields=("date_issued","card_name","card_number","card_type","expiry_date","card_status","security_code","wallet","account","issuer") 

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=("wallet","transaction_amount","transaction_type","transaction_charge","transaction_date","receipt","origin_account","destination_account")              


class LoanSerializer(serializers.ModelSerializer)  :
    class Meta:
        model=Loan
        fields=("loan_number","loan_type","amount","date_and_time","wallet","interest_rate","guarantor","pay_due_date","loan_balance")


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Receipt
        fields=("receipt_type","receipt_date","receipt_file","total_amount")   


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notifications
        fields=("notifications_id","name","status","date_and_time","receipt")




 