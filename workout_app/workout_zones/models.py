from django.db import models


class Hall(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    hall_picture = models.ImageField(
        upload_to="workout/halls_pictures", null=True, blank=True
    )

    def __str__(self) -> str:
        return self.name
