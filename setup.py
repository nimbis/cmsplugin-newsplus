from setuptools import setup, find_packages

# parse requirements
req_lines = [line.strip() for line in open(
    'requirements/common.txt').readlines()]
install_reqs = list(filter(None, req_lines))


# setup the project
setup(
    name='cmsplugin-newsplus',
    version='0.1.6',
    description='Simple news plugin for django-cms 3.x',
    long_description=open('README.rst').read(),
    author='Nimbis Services, Inc.',
    author_email='devops@nimbisservices.com',
    url='https://github.com/nimbis/cmsplugin-newsplus/',
    packages=find_packages(),
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
