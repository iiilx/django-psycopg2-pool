# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-psycopg2-pool',
    version='0.1.1',
    author=u'Ben Lee',
    author_email='ben86lee@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/iiilx/django-psycopg2-pool',
    license='BSD license, see LICENSE.txt',
    description='A db backend for Django using the gevent psycopg2-pool',
    long_description=open('README.md').read(),
    zip_safe=False,
)
