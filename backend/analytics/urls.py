from django.urls import path
from .views import (
    SiteListCreateView,
    SiteDetailView,
    EnergyReadingListCreateView,
    EnergyReadingDetailView,
)

urlpatterns = [
    path("sites/", SiteListCreateView.as_view(), name="site-list-create"),
    path("sites/<int:pk>/", SiteDetailView.as_view(), name="site-detail"),

    path("readings/", EnergyReadingListCreateView.as_view(), name="reading-list-create"),
    path("readings/<int:pk>/", EnergyReadingDetailView.as_view(), name="reading-detail"),
]