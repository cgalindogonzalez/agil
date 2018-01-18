from django.shortcuts import render
from .models import Articles


# Create your views here.
def first_view(request):

    articles = Articles.objects.all
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)
