from django.db import models


class Article(models.Model):
    title = models.CharField(verbose_name='일기 제목', max_length=100)
    content = models.TextField(verbose_name='일기 내용')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}. {self.title}'
