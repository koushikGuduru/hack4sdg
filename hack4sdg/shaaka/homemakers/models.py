from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User

class FoodItem(models.Model):
    homemaker = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food_items/')
    description = models.TextField()

    def __str__(self):
        return self.name