from django.urls import path
from . import views

urlpatterns = [path("myapi/", views.MyApi.as_view())]
