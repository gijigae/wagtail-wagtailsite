from datetime import datetime, time
from django.contrib.syndication.views import Feed

from wagtailsite.models import BlogPage


class BlogFeed(Feed):
    title = "The Wagtail Blog"
    link = "/blog/"
    description = "The latest news and views from the Wagtail team"

    def items(self):
        return BlogPage.objects.live().order_by('-date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.intro if item.intro else item.body

    def item_link(self, item):
        return item.full_url

    def item_author_name(self, item):
        pass

    def item_pubdate(self, item):
        return datetime.combine(item.date, time())
