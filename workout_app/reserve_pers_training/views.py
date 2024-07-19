import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView
from trainers.models import Trainer

from .forms import ReservationForm
from .models import Reserve, Schedule
from .utils import get_schedule_events


class CreateReservationView(LoginRequiredMixin, CreateView):
    model = Reserve
    form_class = ReservationForm
    template_name = "reserve_pers_training/reservation_form.html"
    success_url = reverse_lazy("success_reservation")

    def form_valid(self, form):
        trainer_id = self.kwargs.get("trainer_id")
        trainer = get_object_or_404(Trainer, pk=trainer_id)
        form.instance.user = self.request.user
        form.instance.trainer = trainer

        date = form.cleaned_data["date"]
        start_time = form.cleaned_data["start_time"]
        end_time = form.cleaned_data["end_time"]

        if not Schedule.objects.filter(
            trainer=trainer, date=date, is_working_day=True
        ).exists():
            messages.error(
                self.request,
                "The trainer is not available on this day. Please choose another date.",
            )
            return redirect("create_reservation", trainer_id=trainer.id)

        reservations = Reserve.objects.filter(
            trainer=trainer, date=date, start_time__lt=end_time, end_time__gt=start_time
        )

        if reservations.exists():
            messages.error(
                self.request, "Not available in this time, please choose another time"
            )
            return redirect("create_reservation", trainer_id=trainer.id)

        super().form_valid(form)

        send_mail(
            "Training reservation confirmation",
            f"You booked training with {trainer.name} on {date} from {start_time} to {end_time}.",
            "noreply@yourdomain.com",
            [self.request.user.email],
            fail_silently=False,
        )

        messages.success(self.request, "Successfully reserved.")
        return HttpResponseRedirect(reverse("success_reservation"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trainer = get_object_or_404(Trainer, id=self.kwargs["trainer_id"])
        context["trainer"] = trainer

        events = get_schedule_events(trainer)

        context["events_json"] = json.dumps(events)
        context["events"] = events
        return context


class SuccessReservationView(TemplateView):
    template_name = "reserve_pers_training/success_reservation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["email"] = self.request.user.email
        return context


def get_schedule_events_view(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    events = get_schedule_events(trainer)
    return JsonResponse(events, safe=False)
