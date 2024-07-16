from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from trainers.models import Trainer

from .forms import ReviewForm
from .models import Review


class LeaveReview(CreateView):
    form_class = ReviewForm
    success_url = reverse_lazy("homepage")
    template_name = "review/leave_review.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.trainer = get_object_or_404(Trainer, pk=self.kwargs["trainer_id"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("trainer_detail", kwargs={"pk": self.kwargs["trainer_id"]})


class AllTrainerReviews(ListView):
    model = Review
    template_name = "review/all_reviews.html"
    context_object_name = "reviews"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trainer = get_object_or_404(Trainer, pk=self.kwargs["trainer_id"])
        context["trainer"] = trainer
        return context

    def get_queryset(self):
        self.trainer = get_object_or_404(Trainer, pk=self.kwargs["trainer_id"])
        return Review.objects.filter(trainer=self.trainer)
