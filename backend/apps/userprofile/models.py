from django.db import models
from django.contrib.auth.models import User
from apps.team.models import Team

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} ({self.team})"
