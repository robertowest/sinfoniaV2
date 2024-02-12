from django.db import models

# Create your models here.
class Remesa(models.Model):
    id = models.IntegerField(primary_key=True)
    numero = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'remesas'
