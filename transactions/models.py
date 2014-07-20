from django.db import models

class Transaction(models.Model):
    desc = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    amount = models.FloatField()


class Split(models.Model):
    transaction = models.ForeignKey(Transaction)
    userId = models.CharField(max_length=255)
    split = models.IntegerField()
