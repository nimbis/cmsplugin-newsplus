"""
This module hooks into django-cms' menu system by providing a clear menu
hierarchy for every news item.
"""
from django.utils.translation import ugettext_lazy as _

from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu

from . import navigation


class NewsItemMenu(CMSAttachMenu):
    name = _("News menu")

    def get_nodes(self, request):
        return navigation.get_nodes(request)


menu_pool.register_menu(NewsItemMenu)
