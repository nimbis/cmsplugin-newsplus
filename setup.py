#!/usr/bin/env python

from setuptools import find_packages, setup

# setup the project
setup(
    name='cmsplugin-newsplus',
    version='0.1.9',
    description='Simple news plugin for django-cms 3.x',
    long_description=open('README.rst').read(),
    author='Nimbis Services, Inc.',
    author_email='devops@nimbisservices.com',
    url='https://github.com/nimbis/cmsplugin-newsplus/',
    packages=find_packages(exclude=["tests", ]),
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    install_requires=[
        'Django<1.8',
        'django-cms >= 2.4',
        'djangocms-text-ckeditor >= 2.0',
        'Pillow',
    ],
    zip_safe=False
)
