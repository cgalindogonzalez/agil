from django.shortcuts import render
from .models import Articles


# Create your views here.
def first_view(request):

    articles = Articles.objects.all
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def one_article_view(request, article_id):

    article = Articles.objects.get(pk=article_id)

    context = {'article': article}
    return render(request, 'articles/one_article.html', context)
