from django.urls import path ,include
from rest_framework import routers
from .views import AccountDepositView,AccountTransferView



from .views import AccountViewSet, CardViewSet, CustomerViewset, LoanViewSet, NotificationViewSet, ReceiptViewSet, TransactionViewSet, WalletViewSet

router=routers.DefaultRouter()
router.register(r"customers",CustomerViewset)
router.register(r"wallets",WalletViewSet)
router.register(r"accounts",AccountViewSet)
router.register(r"cards",CardViewSet)
router.register(r"transactions",TransactionViewSet)
router.register(r"loans",LoanViewSet)
router.register(r"receipts",ReceiptViewSet)
router.register(r"notifications",NotificationViewSet)


urlpatterns=[
    path("",include(router.urls)),
    path("deposit/", AccountDepositView.as_view(), name="deposit-view"),
    path("transfer/", AccountTransferView.as_view(), name="transfer-view"),
]
