from typing import cast
from django.db.models import Count
from .models import *
from django.conf import settings


class PostListMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['footer_color'] = settings.LOCAL_STYLES.get('dark-footer-text')
        return context


class PostDetailMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['footer_color'] = settings.LOCAL_STYLES.get(
            'white-footer-text')
        return context

# class UserMixin:
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['footer_color'] = settings.LOCAL_STYLES.get('dark-footer-text')
#         return context

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
]
