from django.db import models

class Transaction(models.Model):
    desc = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    amount = models.FloatField()
    # user id of the person who paid
    # paidby = models.CharField(max_length=255)


class Split(models.Model):
    transaction = models.ForeignKey(Transaction, \
                                    related_name='splits' )
    userid = models.CharField(max_length=255)
    split = models.IntegerField()

    class Meta:
        unique_together = ('transaction', 'userid')
