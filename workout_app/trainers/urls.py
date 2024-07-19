from django.urls import path

from .views import TrainerDetailView, TrainerListView

urlpatterns = [
    path("trainers/", TrainerListView.as_view(), name="trainer_list"),
    path("trainer/<int:pk>", TrainerDetailView.as_view(), name="trainer_detail"),
]
