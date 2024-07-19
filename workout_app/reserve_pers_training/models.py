# models.py
from django.contrib.auth.models import User
from django.db import models
from trainers.models import Trainer


class Reserve(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ("trainer", "date", "start_time", "end_time")

    def __str__(self):
        return f"Schedule for {self.trainer.name} on {self.date} from {self.start_time} to {self.end_time}"


class Schedule(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateField()
    is_working_day = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.trainer.name} - {self.date}"
