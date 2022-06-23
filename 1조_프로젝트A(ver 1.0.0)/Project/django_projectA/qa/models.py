from django.db import models

class context(models.Model):
    ID = models.IntegerField(primary_key = True)
    country = models.CharField(max_length=45)
    country_num = models.CharField(max_length=45)
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'context'


class questions(models.Model):
    ID = models.CharField(primary_key=True, max_length=40)
    context_id = models.IntegerField()
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'questions'
