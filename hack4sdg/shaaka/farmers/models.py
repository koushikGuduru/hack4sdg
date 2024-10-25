from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    quantity = models.IntegerField()
    price_per_quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name