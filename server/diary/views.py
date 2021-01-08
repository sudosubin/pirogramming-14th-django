from django.http import HttpRequest
from django.shortcuts import render

from diary.models import Article


def article_list(request: HttpRequest):
    queryset = Article.objects.all()
    context = {
        "articles": queryset
    }
    return render(request, "diary/list.html", context)
