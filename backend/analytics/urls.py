from django.urls import path
from .upload_views import UploadCSVView
from .views import (
    SiteListCreateView,
    SiteDetailView,
    EnergyReadingListCreateView,
    EnergyReadingDetailView,
)

urlpatterns = [
    path("sites/", SiteListCreateView.as_view(), name="site-list-create"),
    path("sites/<int:pk>/", SiteDetailView.as_view(), name="site-detail"),
    path(
    "readings/upload/",
    UploadCSVView.as_view(),
    name="upload-csv"
),

    path("readings/", EnergyReadingListCreateView.as_view(), name="reading-list-create"),
    path("readings/<int:pk>/", EnergyReadingDetailView.as_view(), name="reading-detail"),
]