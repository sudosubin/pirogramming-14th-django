from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from diary.models import Article


def article_list(request: HttpRequest):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'diary/list.html', context)


def article_read(request: HttpRequest, pk: int):
    try:
        article = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        destination = reverse('diary:article_list')
        return redirect(destination)

    context = {
        'article': article,
    }
    return render(request, 'diary/read.html', context)
