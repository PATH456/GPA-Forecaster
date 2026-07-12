from django.urls import path

from .views import HealthCheckView, TermListCreateView


urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health-check"),
    path("terms/", TermListCreateView.as_view(), name="term-list-create"),
]
