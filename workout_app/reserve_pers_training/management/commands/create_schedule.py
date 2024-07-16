from datetime import date, timedelta

from django.core.management.base import BaseCommand
from reserve_pers_training.models import Schedule
from trainers.models import Trainer


class Command(BaseCommand):
    help = "Generate schedule for trainers"

    def handle(self, *args, **kwargs):
        trainers = Trainer.objects.all()
        start_date = date.today()
        end_date = start_date + timedelta(days=60)

        for trainer in trainers:
            for single_date in (
                start_date + timedelta(n)
                for n in range(0, (end_date - start_date).days + 1, 2)
            ):
                Schedule.objects.create(trainer=trainer, date=single_date)

        self.stdout.write(
            self.style.SUCCESS("Successfully generated schedule for all trainers")
        )
