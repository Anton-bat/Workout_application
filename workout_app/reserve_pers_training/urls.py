from django.urls import path

from .views import CreateReservationView

urlpatterns = [
    path(
        "trainers/<int:trainer_id>/reservations/",
        CreateReservationView.as_view(),
        name="create_reservation",
    ),
]
