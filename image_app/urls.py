from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from image_app import views

urlpatterns = [
    path("images/", views.ImageList.as_view()),
    path("images/<int:pk>/", views.ImageDetail.as_view(), name="image_view"),
]

urlpatterns = format_suffix_patterns(urlpatterns)