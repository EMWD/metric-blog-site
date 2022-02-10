from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('features/', views.FeaturesView.as_view(), name='features'),
    path('donate/', views.DonateView.as_view(), name='donate'),
    path('commands/', views.CommandsView.as_view(), name='commands'),
]