from django.db import models

# Create your models here.
class Train_list(models.Model):
    name = models.CharField(max_length=100)