from django.db import models
from django.contrib.auth.models import User
 
class Team(models.Model):
    name = models.CharField(max_length=250)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def __str__(self) -> str:
        return self.name + " managed by " + str(self.manager)