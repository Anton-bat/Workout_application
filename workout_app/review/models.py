from django.contrib.auth.models import User
from django.db import models
from trainers.models import Trainer


class Review(models.Model):
    review_text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    trainer = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Review for {self.trainer.name} from {self.user.username}"
