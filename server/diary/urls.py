from django.urls import path

from diary.views import article_list

urlpatterns = [
    path('', article_list, name='article_list'),
]
