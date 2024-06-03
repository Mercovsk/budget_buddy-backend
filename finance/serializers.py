from rest_framework import serializers

from finance.models import Cashflow, AccountGroup, Account, Transacation

class CashflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashflow
        fields = "__all__"

class AccountGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountGroup
        fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacation
        fields = "__all__"