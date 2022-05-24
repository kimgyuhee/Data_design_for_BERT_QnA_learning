from django.db import models


class context(models.Model):
    ID = models.IntegerField()
    country = models.CharField(max_length=45)
    country_num = models.CharField(max_length=45)
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'context'
