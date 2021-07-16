from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name