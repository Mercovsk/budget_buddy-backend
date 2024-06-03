from django.db import models

from helper.models import Tracker

CATEGORY = [
    ('inc', 'Income'),
    ('exp', 'Expense'),
]

class Cashflow(Tracker):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY)

    def __repr__(self):
        self.name

    def __str__(self):
        return self.name
    
class AccountGroup(models.Model):
    name = models.CharField(max_length=100)
    
    def __repr__(self):
        self.name

    def __str__(self):
        return self.name

class Account(Tracker):
    name = models.CharField(max_length=100)
    group_id = models.ForeignKey(AccountGroup, on_delete=models.CASCADE, null=True, blank=True)
    groud_order = models.SmallIntegerField(null=True, blank=True)

    def __repr__(self):
        self.name

    def __str__(self):
        return self.name
    
class Transacation(Tracker):
    date_transact = models.DateTimeField()
    amount = models.DecimalField(max_digits=19, decimal_places=10)
    category = models.ForeignKey(Cashflow, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)