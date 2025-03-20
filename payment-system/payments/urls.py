from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = "payments"
urlpatterns = [
    path("", views.index, name="index"),
    path("customer_list/", views.customer_list, name="customer_list"),
    path("lookup_customer/", views.lookup_customer, name="lookup_customer"),
    path("add_customer/", views.add_customer, name="add_customer"),
    path("transaction_list/<int:customer_id>/", views.transaction_list,
         name="transaction_list"),
    path("add_transaction/<int:customer_id>/", views.add_transaction,
         name="add_transaction"),
]
