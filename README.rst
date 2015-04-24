News plugin for django-cms 3.0b3
=================================

.. image:: https://travis-ci.org/nimbis/cmsplugin-newsplus.png?branch=master
  :target: https://travis-ci.org/nimbis/cmsplugin-newsplus

.. image:: https://coveralls.io/repos/nimbis/cmsplugin-newsplus/badge.png?branch=master
  :target: https://coveralls.io/r/nimbis/cmsplugin-newsplus?branch=master



This plugin provides a simple news feature for django-cms 2.4 and newer.

It is based off of a fork of cmsplugin-news located here:
https://bitbucket.org/zerok/cmsplugin-news

The goal of newsplus is to provide the simplicity of cmsplugin-news while
adding some additional functionality, such as images.


Requires
----------------

* django-cms >= 2.4
* django >= 1.5
* djangocms-text-ckeditor >= 2.0


Setup
-----

* Install django-cms (if you haven't done so already)

* Run `pip install cmsplugin-newsplus` or download this package and `python setup.py install`

* Add 'cmsplugin_newsplus' to INSTALLED_APPS

* Add to your project's urls.py:
  ``url(r'^news/', include('cmsplugin_newsplus.urls')),``

* If you're using South run `python manage.py migrate`, Otherwise run
  `python manage.py syncdb` within your project directory.


History
-------

0.1.8:

    * Adding missing Django 1.7 migration.

0.1.7:

    * Removing parsing of requirements from requirements/common.txt from setup.py

0.1.6:

    * Update migrations to Django 1.7

0.1.5:

    * Added missing urls.py step to Setup section of the README.

0.1.2:

    * Fixed compatibility with pip <= 1.1

0.1.1:

    * Compatility fixes for Django 1.6
    * Cleaned up repo.
    * Added Travis integration.

0.1.0:

    * Initial commit.
