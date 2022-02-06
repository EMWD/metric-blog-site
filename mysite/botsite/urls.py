from django.views.generic.edit import DeleteView
from . import views
from django.urls import path

urlpatterns = [
    path('', views.TestView.as_view(), name='home'),
]