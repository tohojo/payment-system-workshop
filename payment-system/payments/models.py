from django.db import models
from django.utils import timezone
from datetime import datetime
from decimal import Decimal as D

class Customer(models.Model):
    name = models.CharField(max_length=200)
    card_number = models.CharField(max_length=200, unique=True)

    @property
    def balance(self):
        balance = D("0.00")

        # TODO: Implement logic here to compute the customer balance
        #       Hint: Customer transactions are in self.transaction_set.all()

        return balance

    def __str__(self):
        return self.name

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    time = models.DateTimeField("transaction time", default=timezone.now)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        ordering = ['time']

    def __str__(self):
        return f"{self.time} {self.customer.name}: {self.description} ({self.amount})"
