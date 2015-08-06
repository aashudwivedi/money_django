from django.db import models

INR = 'INR'
DOLLAR = 'DOLLAR'

currencies = (
    (INR, 'Indian Rupee'),
    (DOLLAR, 'DOLLAR'),
)

class Transaction(models.Model):
    desc = models.CharField(max_length=255)
    currency = models.CharField(max_length=255, choices=currencies)
    amount = models.FloatField()
    creation_time = models.DateTimeField(auto_now=True)
    # user id of the person who paid
    # paidby = models.CharField(max_length=255)


class Split(models.Model):
    transaction = models.ForeignKey(Transaction,
                                    related_name='splits')
    userid = models.CharField(max_length=255)
    amount = models.IntegerField(blank=False)

    class Meta:
        pass #unique_together = ('transaction', 'userid')
