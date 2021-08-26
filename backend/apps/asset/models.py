from django.db import models
""" from ..team.models import Team
from ..supplier.models import Supplier """

# Create your models here.
class Asset(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.TextField()
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    """ supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE) """

    def __str__(self) -> str:
        return f" {self.name}    |   {self.cost} "