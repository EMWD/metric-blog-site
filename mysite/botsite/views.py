from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.views import View, generic
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
# from .models import Post
from icecream import ic
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.conf import settings

from .models import *


class HomeView(generic.ListView):
    queryset = []
    template_name = 'index.html'


class DonateView(generic.ListView):
    queryset = []
    template_name = 'donate.html'


class FeaturesView(generic.ListView):
    queryset = []
    template_name = 'features.html'


class CommandsView(generic.ListView):
    queryset = []
    template_name = 'commands.html'


class AboutView(generic.ListView):
    queryset = []
    template_name = 'about.html'

