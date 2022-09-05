from django.urls import path
from .views import loan, my_account, my_card, my_currency, notifications, receipt, register_customer, reward, third_party, transaction, wallet


urlpatterns = [
    path("register/",register_customer,name="registration"),
    path("wallet/",wallet,name="wallet"),
    path("currency/",my_currency,name="my_currency"),
    path("account/",my_account,name="account"),
    path("transaction/",transaction,name="transaction"),
    path("card/",my_card,name="card"),
    path("thirdparty/",third_party,name="thirdparty"),
    path("notification/",notifications,name="notifications"),
    path("receipt/",receipt,name="receipt"),
    path("loan/",loan,name="loan"),
    path("reward/",reward,name="reward"),
]
