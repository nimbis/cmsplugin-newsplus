from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from .menu import NewsItemMenu


class NewsAppHook(CMSApp):
    name = _('News App')
    urls = ['cmsplugin_newsplus.urls']
    menus = [NewsItemMenu]


apphook_pool.register(NewsAppHook)
