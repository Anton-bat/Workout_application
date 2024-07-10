from django.urls import path

from .views import HallDetailView, HallListView

urlpatterns = [
    path("halls/", HallListView.as_view(), name="hall_list"),
    path("halls/<int:pk>", HallDetailView.as_view(), name="hall_detail"),
]
