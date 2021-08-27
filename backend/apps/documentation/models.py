from django.db import models


class Documentation(models.Model):
    name = models.CharField(max_length=250, unique=True)
    asset = models.CharField(max_length=10)
    description = models.TextField(max_length=500)
    url = models.URLField(max_length=250)
    file = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.name}, {self.asset}, {self.description}, {self.url}, {self.file}"
