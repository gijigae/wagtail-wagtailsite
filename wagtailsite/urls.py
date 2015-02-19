from django.conf.urls import url

from wagtailsite.feeds import BlogFeed

urlpatterns = [
    url(r'^blog/feed/$', BlogFeed(), name='blog_feed')
]
