from django.http import HttpRequest
from django.shortcuts import render


def article_list(request: HttpRequest):
    context = {}
    return render(request, 'diary/list.html', context)
