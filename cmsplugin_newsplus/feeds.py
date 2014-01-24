from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

from . import models
from . import settings


class NewsFeed(Feed):
    title = settings.FEED_TITLE
    description = settings.FEED_DESCRIPTION

    title_template = 'cmsplugin_newsplus/feeds/item_title.html'
    description_template = 'cmsplugin_newsplus/feeds/item_description.html'

    @property
    def link(self):
        return reverse('news_archive_index')

    def items(self):
        return models.News.published.all()[:settings.FEED_SIZE]

    def item_url(self, item):
        return item.get_absolute_url()

    def item_pubdate(self, item):
        return item.pub_date
