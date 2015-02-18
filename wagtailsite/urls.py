from django.conf.urls import url

from wagtailsite.models import BlogFeed

urlpatterns = [
    url(r'^blog/feed/$', BlogFeed())
]
