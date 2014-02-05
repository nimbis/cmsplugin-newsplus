from __future__ import absolute_import
from django import forms
from django.conf import settings

from cms.plugin_pool import plugin_pool
from djangocms_text_ckeditor.widgets import TextEditorWidget
from cmsplugin_newsplus.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News

    def _get_widget(self):
        plugins = plugin_pool.get_text_enabled_plugins(placeholder=None,
                                                       page=None)
        return TextEditorWidget(installed_plugins=plugins)

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        widget = self._get_widget()
        self.fields['excerpt'].widget = widget
        self.fields['content'].widget = widget
