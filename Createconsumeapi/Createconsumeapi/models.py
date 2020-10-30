from django.db import models

class Empmodel(models.Model):
    SOURCE_ACCT=models.CharField(max_length=400, blank=True, null=False,primary_key=True)
    AMOUNT=models.CharField(max_length=400, blank=True, null=False,primary_key=False)
    class Meta:
        db_table='CHANNEL_BILLS_FINAL'
   