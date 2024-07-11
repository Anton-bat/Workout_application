import json

from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from trainers.models import Trainer

from .forms import ReservationForm
from .models import Schedule


class CreateReservationView(CreateView):
    model = Schedule
    form_class = ReservationForm
    template_name = "your_app/reservation_form.html"
    success_url = reverse_lazy("trainer_detail")

    def form_valid(self, form):
        trainer = get_object_or_404(Trainer, id=self.kwargs["trainer_id"])
        form.instance.trainer = trainer
        form.instance.user = self.request.user

        # Перевірка на перетин часу
        date = form.cleaned_data["date"]
        start_time = form.cleaned_data["start_time"]
        end_time = form.cleaned_data["end_time"]
        reservations = Schedule.objects.filter(
            trainer=trainer, date=date, start_time__lt=end_time, end_time__gt=start_time
        )

        if reservations.exists():
            messages.error(
                self.request, "Not available in this time, please choose other time"
            )
            return redirect("create_reservation", trainer_id=trainer.id)

        # Виклик методу save форми для збереження даних
        response = super().form_valid(form)

        # Відправка підтвердження на email
        send_mail(
            "Training reservation confirmation",
            f"You booked training with {trainer.name} on {date} since {start_time} till {end_time}.",
            "noreply@yourdomain.com",
            [self.request.user.email],
            fail_silently=False,
        )

        messages.success(self.request, "Succesfully reserved.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trainer"] = get_object_or_404(Trainer, id=self.kwargs["trainer_id"])
        return context

    def get_schedule_events(request, trainer_id):
        trainer = Trainer.objects.get(id=trainer_id)
        schedules = Schedule.objects.filter(trainer=trainer, is_working_day=True)

        events = []
        for schedule in schedules:
            events.append(
                {
                    "title": f"Available",
                    "start": f"{schedule.date}T08:00:00",
                    "end": f"{schedule.date}T19:00:00",
                }
            )

        return JsonResponse(events, safe=False)
