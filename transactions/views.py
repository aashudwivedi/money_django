from django.shortcuts import render

from transactions.models import Transaction, Split
from rest_framework import viewsets
from transactions.serializers import TransactionSerializer, \
     SplitSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class SplitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Split.objects.all()
    serializer_class = SplitSerializer
