cmsplugin-newsplus
=================================

[![Build Status](https://travis-ci.org/nimbis/cmsplugin-newsplus.svg?branch=master)](https://travis-ci.org/nimbis/cmsplugin-newsplus)

[![Coverage Status](https://coveralls.io/repos/nimbis/cmsplugin-newsplus/badge.svg?branch=master&service=github)](https://coveralls.io/github/nimbis/cmsplugin-newsplus?branch=master)

This plugin provides a simple news feature for django-cms 2.4 and newer.

It is based off of a fork of cmsplugin-news located here:
https://bitbucket.org/zerok/cmsplugin-news

The goal of newsplus is to provide the simplicity of cmsplugin-news while
adding some additional functionality, such as images.


Requires
----------------

* django-cms >= 3.3
* django >= 1.8
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

Contributing
------------

See the [Contributing Guidelines](CONTRIBUTING.md).

History
-------

1.1.0 (December 7, 2017):

    * Add url namespaces for Django >1.8.  Much thanks to jrutila (https://github.com/jrutila) for this contribution!

1.0.1 (December 7, 2017):

    * Fix travis-testing makefile target.
    * Limit Django support to <2.0.

0.1.10:

    * Adding Django 1.8 support by specifying fields in NewsForm.

0.1.9:

    * Removing broken migration introduced in v0.1.8 and replacing it with a working one.

0.1.8:

    * Adding missing Django 1.7 migration. This version should not be used because the migration added in this version was broken. The default publication date was datetime.now() which was being evaluated each time makemigrations would be called.

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
