from setuptools import setup, find_packages


base_requirements = [
    'django-cms >= 2.0, < 3.0'
]
install_requirements = base_requirements + []
test_requirements = base_requirements + [
    'PIL',
]


setup(
    name='cmsplugin-news',
    version='0.4.2',
    description='Simple news plugin for django-cms 2.x',
    long_description=open('README.rst').read(),
    author='Horst Gutmann',
    author_email='zerok@zerokspot.com',
    url='http://bitbucket.org/zerok/cmsplugin-news/',
    packages=find_packages(),
    package_data={'cmsplugin_news': [
        'locale/de/LC_MESSAGES/*',
        'templates/cmsplugin_news/*.html',
        'templates/cmsplugin_news/feeds/*.html',
        'templates/cmsplugin_news/widgets/*.html']
    },
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
    install_requires=install_requirements,
    tests_require=test_requirements,
    test_suite='runtests.main',
    zip_safe=False
)
