from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places = 2)
    nid = models.IntegerField(default=0, unique=True,validators=[MaxValueValidator(999999999999)])

    def __str__(self):
        return str(self.account_no) 