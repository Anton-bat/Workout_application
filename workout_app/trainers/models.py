from django.db import models
from workout_zones.models import Hall


class Trainer(models.Model):
    name = models.CharField(max_length=50)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to="workout/profile_pictures", null=True, blank=True
    )

    def __str__(self) -> str:
        return self.name
