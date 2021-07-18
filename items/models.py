from django.db import models
from django.contrib.auth import get_user_model        #new

User = get_user_model()        #new


class Item(models.Model):        #new
    name = models.CharField(max_length=50, unique=True)        #new
    description = models.TextField(max_length=250)        #new
    price = models.DecimalField(max_digits=14, decimal_places=2)        #new
    user = models.ForeignKey(User, on_delete=models.CASCADE)        #new

    def __str__(self):        #new
        return self.name        #new