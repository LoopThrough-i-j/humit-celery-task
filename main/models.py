from django.db import models

# Create your models here.

class Logs(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=1000)
