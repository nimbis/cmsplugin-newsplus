from datetime import datetime
import logging
from django.core.urlresolvers import reverse

from menus.base import NavigationNode

from cmsplugin_newsplus.models import News


logger = logging.getLogger(__name__)


def get_nodes(request):
    logger.debug("Rebuilding news menu")
    res = []

    items = News.published.all()

    years_done = []
    months_done = []
    days_done = []
    slug_done = []

    for item in items:
        date = item.pub_date

        if date.year not in years_done:
            years_done.append(date.year)
            year_node = NavigationNode(date.year,
                                       reverse('news_archive_year',
                                               kwargs=dict(year=date.year)),
                                       'newsitem-year-%d' % (date.year,))
            year_node.childrens = []
            months_done = []
            res.append(year_node)

        if date.month not in months_done:
            months_done.append(date.month)
            month_node = NavigationNode(
                datetime.strftime(date, '%B'),
                reverse('news_archive_month', kwargs=dict(
                    year=date.year,
                    month=datetime.strftime(date, '%m'))),
                'newsitem-month-%d.%d' % (
                    date.year,
                    date.month))
            month_node.childrens = []
            days_done = []
            year_node.childrens.append(month_node)

        if date.day not in days_done:
            days_done.append(date.day)
            day_node = NavigationNode(
                datetime.strftime(date, '%d'),
                reverse('news_archive_day', kwargs=dict(
                    year=date.year,
                    month=datetime.strftime(date, '%m'),
                    day=datetime.strftime(date, '%d'))),
                'newsitem-day-%d.%d.%d' % (date.year, date.month, date.day)
                )
            day_node.childrens = []
            slug_done = []
            month_node.childrens.append(day_node)

        if item.slug not in slug_done:
            slug_done.append(item.slug)
            item_node = NavigationNode(
                item.title, item.get_absolute_url(),
                'newsitem-pk-%s' % (str(item.pk),))
            item_node.childrens = []
            day_node.childrens.append(item_node)

    return res
