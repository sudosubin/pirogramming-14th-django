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


def article_create(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'diary/create.html')

    title = request.POST['title']
    content = request.POST['content']

    article = Article.objects.create(title=title, content=content)
    pk = article.id

    destination = reverse('diary:article_read', kwargs={'pk': pk})
    return redirect(destination)


def article_update(request: HttpRequest, pk: int):
    if request.method == 'GET':
        try:
            article = Article.objects.get(id=pk)
        except Article.DoesNotExist:
            destination = reverse('diary:article_list')
            return redirect(destination)

        context = {
            'article': article,
        }
        return render(request, 'diary/update.html', context)

    title = request.POST['title']
    content = request.POST['content']

    article = Article.objects.filter(id=pk).update(title=title, content=content)

    destination = reverse('diary:article_read', kwargs={'pk': pk})
    return redirect(destination)
