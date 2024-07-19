from django.shortcuts import render
from django.views.generic import DetailView, ListView
from trainers.models import Trainer

from .models import Hall


class HallListView(ListView):
    model = Hall
    template_name = "workout_zones/hall_list.html"
    context_object_name = "halls"


class HallDetailView(DetailView):
    model = Hall
    template_name = "workout_zones/hall_detail.html"
    context_object_name = "hall"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trainers"] = Trainer.objects.filter(hall=self.object)
        return context
