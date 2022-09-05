import re
from django.shortcuts import render
from .forms import AccountForm, CardForm, CurrencyForm, CustomerRegistrationForm, LoanForm, NotificationsForm, ReceiptForm, RewardForm, ThirdPartyForm, TransactionForm, WalletForm

# Create your views here.
def register_customer(request):
    form=CustomerRegistrationForm()
    return render (request,"register_customer.html",{"form":form})


def wallet(request):
    form=WalletForm()  
    return render(request,"wallet.html",{"form":form})  


def my_currency(request):
    form=CurrencyForm()
    return render (request,"currency.html",{"form":form})


def my_account(request):
    form=AccountForm()
    return render (request,"account.html",{"form":form})


def transaction(request):
    form=TransactionForm()
    return render (request,"transaction.html",{"form":form})    

def my_card(request):
    form=CardForm()
    return render (request,"card.html",{"form":form})    

def third_party(request):
    form=ThirdPartyForm()
    return render (request,"thirdparty.html",{"form":form})  

def notifications(request):
    form=NotificationsForm()
    return render (request,"notifications.html",{"form":form}) 

def receipt(request)   :
    form=ReceiptForm()  
    return render (request,"receipt.html",{"form":form})    


def loan(request)   :
    form=LoanForm()
    return render (request,"loan.html",{"form":form}) 


def reward(request):
    form=RewardForm()
    return render(request,"reward.html",{"form":form})    