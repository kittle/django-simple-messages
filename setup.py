#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = "django-simple-messages",
    version = "0.0.1",
    description = "YA django messages",
    author = "Andrey Gerzhov",
    author_email = "kittle@humgat.org",
    license = "BSD License",
    url = "https://github.com/kittle/django-simple-messages",
    packages = ["simple_messages"],
    # package_data = {"": ["templates/*"]},
    long_description = "",
    #install_requires=[
    #   'requests==0.14.1',
    #   ]
)
