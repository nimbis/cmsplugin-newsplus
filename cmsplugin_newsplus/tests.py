"""
Tests for the cmsplugin_newsplus
"""
from django.test import TestCase
from cmsplugin_newsplus.models import News
from django.utils.timezone import utc
from . import settings
import datetime


class NewsTest(TestCase):
    urls = 'cmsplugin_newsplus.urls'

    def setUp(self):
        self.today = datetime.datetime.today().replace(tzinfo=utc)
        self.yesterday = self.today - datetime.timedelta(days=1)
        self.tomorrow = self.today + datetime.timedelta(days=1)

    def tearDown(self):
        pass

    def test_unpublished(self):
        """
            Test if unpublished items are hidden by default
        """
        unpublished = News.objects.create(
            title='Unpublished News',
            slug='unpublished-news',
            is_published=False,
            pub_date=self.yesterday,
        )
        self.assertEquals(unpublished.__unicode__(), 'Unpublished News')
        self.assertEquals(News.published.count(), 0)
        unpublished.is_published = True
        unpublished.save()
        self.assertEquals(News.published.count(), 1)
        unpublished.is_published = False
        unpublished.save()
        self.assertEquals(News.published.count(), 0)
        unpublished.delete()

    def test_future_published(self):
        """
            Tests that items with a future published date are hidden
        """
        future_published = News.objects.create(
            title='Future published News',
            slug='future-published-news',
            is_published=True,
            pub_date=self.tomorrow,
        )
        self.assertEquals(News.published.count(), 0)
        future_published.pub_date = self.yesterday
        future_published.save()
        self.assertEquals(News.published.count(), 1)
        future_published.pub_date = self.tomorrow
        future_published.save()
        self.assertEquals(News.published.count(), 0)

    def test_navigation(self):
        """
            Tests if the navigation build by navigation.get_nodes is correct
        """
        pass

    def test_link_as_url_without_content(self):
        """
        If the news item contains a link but no content and
        USE_LINK_ON_EMPTY_CONTENT_ONLY as well as LINK_AS_ABSOLUTE_URL are
        enabled use this link as absolute url for the item.
        """
        settings.USE_LINK_ON_EMPTY_CONTENT_ONLY = True
        settings.LINK_AS_ABSOLUTE_URL = True
        item = News.objects.create(
            title='Future published News',
            slug='future-published-news',
            is_published=True,
            pub_date=self.tomorrow,
            link='http://lala.com/'
        )
        self.assertEquals('http://lala.com/', item.get_absolute_url())

    def test_link_as_url_with_content(self):
        """
        Same as above, but this time the news item actually has a content
        and should therefor not use the provided link.
        """
        settings.USE_LINK_ON_EMPTY_CONTENT_ONLY = True
        settings.LINK_AS_ABSOLUTE_URL = True
        item = News.objects.create(
            title='Future published News',
            slug='future-published-news',
            content='test',
            is_published=True,
            pub_date=self.tomorrow,
            link='http://lala.com/'
        )
        self.assertNotEquals('http://lala.com/', item.get_absolute_url())
