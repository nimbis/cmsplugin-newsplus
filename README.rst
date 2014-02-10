News plugin for django-cms 3.0b3
=================================

.. image:: https://travis-ci.org/nimbis/cmsplugin-newsplus.png?branch=master
  :target: https://travis-ci.org/nimbis/cmsplugin-newsplus

.. image:: https://coveralls.io/repos/nimbis/cmsplugin-newsplus/badge.png?branch=develop
  :target: https://coveralls.io/r/nimbis/cmsplugin-newsplus?branch=develop



This plugin provides a simple news feature for django-cms 3.0b3 and newer.

It is based off of a fork of cmsplugin-news located here:
https://bitbucket.org/zerok/cmsplugin-news

The goal of newsplus is to provide the simplicity of cmsplugin-news while
added some additional functionality, such as images.


Requires
----------------

* django-cms >= 2.4
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


History
-------

0.1.2:
    * Fixed compatibility with pip <= 1.1

0.1.1:
    * Compatility fixes for Django 1.6
    * Cleaned up repo.
    * Added Travis integration.

0.1.0:
    * Initial commit.
