from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name
