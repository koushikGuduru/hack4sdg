from django.db import models

# Create your models here.


from django.db import models

class Donation(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name