from django.urls import path
from . import views

urlpatterns = [
    path("myapi/", views.MyApi.as_view()),
    path("mashina/", views.MashinaApi.as_view()),
    path("mashina/<int:pk>/", views.MashinaDetailApiView.as_view()),
]
