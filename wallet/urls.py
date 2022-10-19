from unicodedata import name
from django.urls import path
from .views import account_profile, card_profile, customer_profile, edit_account, edit_card, edit_profile, edit_receipt, edit_transaction, edit_wallet, list_account, list_card, list_currency, list_customer, list_loan, list_notifications, list_receipt, list_reward, list_thirdparty, list_transaction, list_wallet, loan, my_account, my_card, my_currency, notifications, receipt, receipt_profile, register_customer, reward, third_party, transaction, transaction_profile, wallet, wallet_profile


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
    path("customers/",list_customer,name="customer_list"),
    path("wallets/",list_wallet,name="wallet_list"),
    path("currencies/",list_currency,name="currency_list"),
    path("accounts/",list_account,name="account_list"),
    path("transactions/",list_transaction,name="transaction_list"),
    path("cards/",list_card,name="card_list"),
    path("thirdparties/",list_thirdparty,name="thirdparty_list"),
    path("notifications/",list_notifications,name="notifications_list"),
    path("receipts/",list_receipt,name="receipt_list"),
    path("loans/",list_loan,name="loan_list"),
    path("rewards/",list_reward,name="rewards_list"),
    path("customers/<int:id>/",customer_profile,name="customer_profile"),
    path("customers/edit/<int:id>/",edit_profile,name="edit_profile"),
    path("wallets/<int:id>/",wallet_profile,name="wallet_profile"),
    path("wallets/edit/<int:id>/",edit_wallet,name="edit_wallet"),
    path("accounts/<int:id>/",account_profile,name="account_profile"),
    path("accounts/edit/<int:id>/",edit_account,name="edit_account"),
    path("cards/<int:id>/",card_profile,name="card_profile"),
    path("cards/edit/<int:id>/",edit_card,name="edit_account"),
    path("transactions/<int:id>/",transaction_profile,name="transaction_profile"),
    path("transactions/edit/<int:id>/",edit_transaction,name="edit_transaction"),
    path("receipts/<int:id>/",receipt_profile,name="receipt_profile"),
    path("receipts/edit/<int:id>/",edit_receipt,name="edit_receipt"),
    
]

