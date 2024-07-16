from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("registration/", include("registration.urls")),
    path("halls/", include("workout_zones.urls")),
    path("trainers/", include("trainers.urls")),
    path("reserve/", include("reserve_pers_training.urls")),
    path("review/", include("review.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
