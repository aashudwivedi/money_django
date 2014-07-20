from transactions.models import Transaction, Split
from rest_framework import serializers

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('desc', 'currency', 'amount')

class SplitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Split
        fields = ('userid', 'split')