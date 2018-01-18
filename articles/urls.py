from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.first_view, name="v"),
    url(r'/(?P<article_id>\d+)/$', views.one_article_view,
        name="one_article"),
]
