from django.http.response import HttpResponseNotAllowed
from django.views import View, generic
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Post
from icecream import ic
from .utils import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.conf import settings

from .forms import *
from .models import *
from .utils import *


class PostListView(PostListMixin, generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetailView(PostDetailMixin, generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def test_access(request):
    access = False
    if settings.ADMIN.get('name') == request.user.username:
        access = True
    ic(request.user.username)
    ic(access)
    return access


class AddPostView(CreateView):

    form_class = AddPostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if test_access(self.request):
            form.save(commit=False)
            return super(AddPostView, self).form_valid(form)
        else:
            return HttpResponseNotAllowed('Only for admin')


class AboutPageView(TemplateView):
    template_name = 'about.html'


class PolicyPageView(TemplateView):
    template_name = 'policy.html'


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
