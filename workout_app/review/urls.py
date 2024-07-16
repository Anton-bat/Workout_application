from django.urls import path

from .views import AllTrainerReviews, LeaveReview

urlpatterns = [
    path(
        "trainers/<int:trainer_id>/reviews/new/",
        LeaveReview.as_view(),
        name="leave_review",
    ),
    path(
        "trainers/<int:trainer_id>/reviews/",
        AllTrainerReviews.as_view(),
        name="all_reviews",
    ),
]
