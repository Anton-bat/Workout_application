from datetime import date, timedelta

from django.shortcuts import render
from django.views.generic import DetailView, ListView
from reserve_pers_training.models import Reserve

from .models import Trainer


class TrainerListView(ListView):
    model = Trainer
    template_name = "trainers/trainer_list.html"
    context_object_name = "trainers"


class TrainerDetailView(DetailView):
    model = Trainer
    template_name = "trainers/trainer_detail.html"
    context_object_name = "trainer"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trainer = self.get_object()
        reservations = Reserve.objects.filter(trainer=trainer)
        context["reservations"] = reservations

        start_date = date.today()
        end_date = start_date + timedelta(days=30)
        trainer_working_days = []
        for single_date in (
            start_date + timedelta(n) for n in range((end_date - start_date).days)
        ):
            if (single_date - start_date).days % 2 == 0:
                trainer_working_days.append({"date": single_date})

        context["trainer_working_days"] = trainer_working_days
        return context
