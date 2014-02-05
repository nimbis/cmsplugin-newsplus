News plugin for django-cms 3.0b3
===============================

This plugin provides a simple news feature for django-cms 3.0b3 and newer.

It is based off of a fork of cmsplugin-news located here:
https://bitbucket.org/zerok/cmsplugin-news

The goal of newsplus is to provide the simplicity of cmsplugin-news while
added some additional functionality, such as images.


Requires
----------------

* django-cms >= 3.0b3
* django >= 1.5
* djangocms-text-ckeditor >= 2.0


Setup
-----

* Install django-cms (if you haven't done so already)

* Download this package and run `python setup.py install` or add it in
  some other way to your current PYTHON_PATH

* Add 'cmsplugin_newsplus' to INSTALLED_APPS

* If you're using South execute `python manage.py migrate`, Otherwise run
  `python manage.py syncdb` within your project directory.

* In order to integrate the news-plugin with your website, create a page and add
  the news application (and optionally the news menu) to it by modifying the
  relevant "advanced settings" of it.


Last Tested With
----------------

* django-cms: 3.0b3
* django: 1.5 and 1.6.1
* djangocms-text-ckeditor: 2.0.5


History
-------

0.1:
    * Initial commit. Compatibility fixes.
