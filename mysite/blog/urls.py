from django.views.generic.edit import DeleteView
from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('delete_post/<slug>/', views.DeletePostView.as_view(), name='delete_post'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('policy/', views.PolicyPageView.as_view(), name='policy'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('video/', views.test_video, name='video'),
]