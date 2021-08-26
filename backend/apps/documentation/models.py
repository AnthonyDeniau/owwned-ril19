from django.db import models


class Documentation(models.Model):
    name = models.TextFeild(max_length=250)
    asset = models.TextFeild(max_length=10)
    description = models.TextFeild(max_length=500)
    URL = models.TextFeild(max_length=250)
    file = models.TextFeild(max_length=250)

    def __str__(self) -> str:
        return f"{self.name}, {self.asset}, {self.description}, {self.URL}, {self.file}"

