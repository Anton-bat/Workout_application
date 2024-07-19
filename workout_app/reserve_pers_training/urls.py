from django.urls import path

from .views import (
    CreateReservationView,
    SuccessReservationView,
    get_schedule_events_view,
)

urlpatterns = [
    path(
        "<int:trainer_id>/",
        CreateReservationView.as_view(),
        name="create_reservation",
    ),
    path(
        "<int:trainer_id>/events/",
        get_schedule_events_view,
        name="get_schedule_events",
    ),
    path(
        "success_reservation/",
        SuccessReservationView.as_view(),
        name="success_reservation",
    ),
]
