from django.conf.urls import url

from wagtailsite.feeds import BlogFeed

def divide_by_zero(request):
    a = 1
    b = 0

    return a / b

urlpatterns = [
    url(r'^blog/feed/$', BlogFeed(), name='blog_feed'),
    url(r'^divide_by_zero$', divide_by_zero),
]
