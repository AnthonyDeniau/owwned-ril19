from django.db import models
from .models import Team

# Create your models here.
class Asset(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.TextField()
    cost = models.DecimalField()
    supplier = models.CharField()

    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name,self.description,self.picture,self.cost,self.supplier