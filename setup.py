from setuptools import setup
from pip.req import parse_requirements

# parse requirements
reqs = parse_requirements("requirements/common.txt")

# setup the project
setup(
    name='cmsplugin-newsplus',
    version='0.1.1',
    description='Simple news plugin for django-cms 3.x',
    long_description=open('README.rst').read(),
    author='Eric Amador',
    author_email='eric.amador14@gmail.com',
    url='https://github.com/amadornimbis/cmsplugin-newsplus/',
    packages=['cmsplugin_newsplus'],
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
    install_requires=[str(x).split(' ')[0] for x in reqs],
    zip_safe=False
)
