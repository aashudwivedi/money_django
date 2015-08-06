from transactions.models import Transaction, Split
from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedRelatedField
from rest_framework.serializers import \
     HyperlinkedModelSerializer

class SplitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Split
        fields = ('userid', 'amount')
            
class TransactionSerializer(serializers.ModelSerializer):
    splits = SplitSerializer(many=True)
    
    class Meta:
        model = Transaction
        fields = ('desc', 'currency', 'amount', 'splits', 'creation_time')

    @transaction.atomic
    def create(self, validated_data):
        return self.save_nested(validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        return self.save_nested(validated_data)

    def save_nested(self, validated_data):
        splits = validated_data.pop('splits')

        transaction = Transaction.objects.create(**validated_data)
        for split in splits:
            spilts_obj, created = Split.objects.update_or_create(
                transaction=transaction, **split)
        return transaction

