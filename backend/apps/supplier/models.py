from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=250)
    website = models.URLField(max_length=200)
    login = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
