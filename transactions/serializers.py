from transactions.models import Transaction, Split
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedRelatedField
from rest_framework.serializers import \
     HyperlinkedModelSerializer

class SplitSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Split
        fields = ('transaction', 'userid', 'split')
            
class TransactionSerializer(serializers.ModelSerializer):
    splits = HyperlinkedRelatedField(many=True, \
                                    view_name='split-detail')
    
    class Meta:
        model = Transaction
        fields = ('desc', 'currency', 'amount', 'splits')
