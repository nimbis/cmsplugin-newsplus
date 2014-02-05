from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils.timezone import utc
import datetime

from cms.models import CMSPlugin

from . import settings


class PublishedNewsManager(models.Manager):
    """
        Filters out all unpublished and items with a publication
        date in the future
    """
    def get_query_set(self):
        return super(PublishedNewsManager, self).get_query_set() \
            .filter(is_published=True) \
            .filter(
                pub_date__lte=datetime.datetime.utcnow().replace(tzinfo=utc))


class News(models.Model):
    """
    News
    """

    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'), unique_for_date='pub_date',
                            help_text=_('A slug is a short name which uniquely'
                                        ' identifies the news item for this'
                                        ' day'))
    excerpt = models.TextField(_('Excerpt'), blank=True)
    content = models.TextField(_('Content'), blank=True)

    is_published = models.BooleanField(_('Published'), default=False)
    pub_date = models.DateTimeField(
        _('Publication date'),
        default=datetime.datetime.utcnow().replace(tzinfo=utc))

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    published = PublishedNewsManager()
    objects = models.Manager()

    link = models.URLField(_('Link'), blank=True, null=True,
                           help_text=_('This link will be used a absolute url'
                                       ' for this item and replaces the view'
                                       ' logic. <br />Note that by default'
                                       ' this only applies for items with '
                                       ' an empty "content" field.'))

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        ordering = ('-pub_date', )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        if settings.LINK_AS_ABSOLUTE_URL and self.link:
            if settings.USE_LINK_ON_EMPTY_CONTENT_ONLY and not self.content:
                return self.link
        return reverse('news_detail',
                       kwargs={'year': self.pub_date.strftime("%Y"),
                               'month': self.pub_date.strftime("%m"),
                               'day': self.pub_date.strftime("%d"),
                               'slug': self.slug})


class NewsImage(models.Model):
    news = models.ForeignKey(News, related_name='images')
    image = models.ImageField(upload_to="news_images")


class LatestNewsPlugin(CMSPlugin):
    """
        Model for the settings when using the latest news cms plugin
    """
    limit = models.PositiveIntegerField(_('Number of news items to show'),
                                        help_text=_('Limits the number of '
                                                    'items that will be '
                                                    'displayed'))
