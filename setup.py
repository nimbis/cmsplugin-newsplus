from setuptools import setup

# parse requirements
req_lines = [line.strip() for line in open(
    'requirements/common.txt').readlines()]
install_reqs = list(filter(None, req_lines))


print req_lines
print install_reqs

# setup the project
setup(
    name='cmsplugin-newsplus',
    version='0.1.2',
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
    install_requires=install_reqs,
    zip_safe=False
)
