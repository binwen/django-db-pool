# -*- coding: utf-8 -*-
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools import find_packages

__version__ = '0.0.3'

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    readme = f.read()

setup(
    name='django-database-pool',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/binwen/django-db-pool',
    license='MIT License',
    author='binwen',
    author_email='cwb201314@qq.com',
    description='通过DBUtils库实现Django数据库连接池，目前支持mysql、postgresql 数据库.',
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        'Topic :: Database',
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    install_requires=[
        'Django>=1.9.9',
        'DBUtils>=1.3',
        'six'
    ]
)
